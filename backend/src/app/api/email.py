from rest_framework.decorators import api_view, authentication_classes, permission_classes
from app.utils.responseutils import send_success_response, send_error_response
from django.core.mail import BadHeaderError, get_connection, send_mass_mail
import threading

from app.models.subscriber import SubscriberModel
from app.models.company import CompanyModel
from app.models.email_config import EmailConfigModel
from app.models.email import EmailModel
from app.serializers.email_config import EmailConfigSerializer
from app.serializers.email import EmailSerializer


# Config Email Settings
# Url: http://<your-domain>/api/v1/email/config
# Method: POST
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def config_email(request):
    return create(request)

# Send Email
# Url: http://<your-domain>/api/v1/email/
# Method: POST
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def send_email(request):
    return send_mail_task(request)

class EmailThread(threading.Thread):
    def __init__(self, messages, config, email):
        self.messages = messages
        self.config = config
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        with get_connection(
                username=self.config.email_sender,
                password=self.config.email_password,
                host=self.config.smtp_server,
                port=self.config.smtp_port,
                use_tls=True
        ) as connection:
            try:
                send_mass_mail(self.messages, fail_silently=True, connection=connection)
                self.email.status = "COMPLETE"
            except BadHeaderError:
                self.email.status = "ERROR"
        self.email.save()

#Create Email Configuration
def create(request):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    config = EmailConfigModel(company=company)
    serializer = EmailConfigSerializer(config, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return send_success_response(msg="Email Configuration Created Successfully", payload=serializer.data)
    return send_error_response(msg="Validation Error", payload=serializer.errors)

# Send Mail
def send_mail_task(request):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    subject = request.data['subject']
    message = request.data['message']
    groups = request.data['groups']
    subscribers = request.data['subscribers']
    subscriber_emails = SubscriberModel.objects.none()

    if subject and message and (groups or subscribers):

        for group_id in groups:
            receivers_list = SubscriberModel.objects.filter(company=company, group=group_id,
                                                            status='ACTIVE').values_list('email', flat=True)
            subscriber_emails = subscriber_emails | receivers_list

        for subscriber_id in subscribers:
            receiver = SubscriberModel.objects.filter(company=company, id=subscriber_id, status='ACTIVE').values_list(
                'email', flat=True)
            subscriber_emails = subscriber_emails | receiver

        subscriber_emails = subscriber_emails.distinct()
        return save_and_send_mail(company, groups, subscribers, subject, message, subscriber_emails)

    else:
        return send_error_response(msg="Make sure all fields are entered and valid.")

def save_and_send_mail(company, groups, subscribers, subject, message, subscriber_emails):
    config = EmailConfigModel.objects.get(company=company, status='ACTIVE')
    mail_from = config.email_sender
    email = EmailModel(company=company)
    group_str = ', '.join(map(str, groups))
    subscribers_str = ', '.join(map(str, subscribers))

    serializer = EmailSerializer(email, data={'subject': subject, 'message': message, 'groups': group_str,
                                              'subscribers': subscribers_str, 'status': "SCHEDULED"})
    messages = [(subject, message, mail_from, [recipient]) for recipient in subscriber_emails]

    if serializer.is_valid():
        serializer.save()
        EmailThread(messages, config, email).start()
        return send_success_response(msg="Emails send and save successfully")

    return send_error_response(msg="Validation Error", payload=serializer.errors)