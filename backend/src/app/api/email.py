from rest_framework.decorators import api_view, authentication_classes, permission_classes
from app.utils.responseutils import send_success_response, send_error_response
from celery import shared_task

from app.models.company import CompanyModel
from app.models.email_config import EmailConfigModel
from app.models.email import EmailModel
from app.serializers.email_config import EmailConfigSerializer
from app.serializers.email import EmailSerializer
from app.api.tasks import send_mail_task


# Config Email Settings
# Url: http://<your-domain>/api/v1/email/config
# Method: POST
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def config_email(request):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    config = EmailConfigModel(company=company)
    serializer = EmailConfigSerializer(config, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return send_success_response(msg="Email Configuration Created Successfully", payload=serializer.data)
    return send_error_response(msg="Validation Error", payload=serializer.errors)


# Send Email
# Url: http://<your-domain>/api/v1/email/
# Method: POST
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
@shared_task()
def send_email(request):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    subject = request.data['subject']
    message = request.data['message']
    groups = request.data['groups']
    subscribers = request.data['subscribers']
    if subject and message and (groups or subscribers):

        email = EmailModel(company=company)
        group_str = ', '.join(map(str, groups))
        subscribers_str = ', '.join(map(str, subscribers))
        serializer = EmailSerializer(email, data={'subject': subject, 'message': message, 'groups': group_str,
                                                  'subscribers': subscribers_str, 'status': "SCHEDULED"})
        if serializer.is_valid():
            serializer.save()
            send_mail_task.delay(subject, message, groups, subscribers, request.company_id, email.id)
            return send_success_response(msg="Emails send and save successfully")
        return send_error_response(msg="Validation Error", payload=serializer.errors)
    else:
        return send_error_response(msg="Make sure all fields are entered and valid.")
