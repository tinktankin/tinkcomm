from celery import shared_task
from django.core.mail import BadHeaderError, get_connection, send_mass_mail

from app.utils.responseutils import send_error_response, send_success_response
from app.models.company import CompanyModel
from app.models.subscriber import SubscriberModel
from app.models.email_config import EmailConfigModel
from app.models.email import EmailModel

@shared_task
def send_mail_task(subject, message, groups, subscribers, company_id, email_id):
    company = CompanyModel.objects.get(id=company_id, status='ACTIVE')
    config = EmailConfigModel.objects.get(company=company, status='ACTIVE')
    mail_from = config.email_sender
    subscriber_emails = SubscriberModel.objects.none()

    for group_id in groups:
        receivers_list = SubscriberModel.objects.filter(company=company, group=group_id,
                                                        status='ACTIVE').values_list('email', flat=True)
        subscriber_emails = subscriber_emails | receivers_list

    for subscriber_id in subscribers:
        receiver = SubscriberModel.objects.filter(company=company, id=subscriber_id, status='ACTIVE').values_list(
            'email', flat=True)
        subscriber_emails = subscriber_emails | receiver

    subscriber_emails = subscriber_emails.distinct()
    email = EmailModel.objects.get(company=company, id=email_id)
    with get_connection(
        username=config.email_sender,
        password=config.email_password,
        host=config.smtp_server,
        port=config.smtp_port,
        use_tls=True
    ) as connection:
        try:
            messages = [(subject, message, mail_from, [recipient]) for recipient in subscriber_emails]
            total_mail = send_mass_mail(messages, fail_silently=True, connection=connection)
        except BadHeaderError:
            email.status = "ERROR"
            email.save()
            return send_error_response(msg="Invalid header found")

        if total_mail == 0 and subscriber_emails != 0:
            email.status = "ERROR"
            email.save()
        email.status = "COMPLETE"
        email.save()
        return send_success_response(msg="Emails send successfully")



