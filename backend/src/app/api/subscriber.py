from rest_framework.decorators import api_view, authentication_classes, permission_classes

from app.models.company import CompanyModel
from app.models.subscriber import SubscriberModel
from app.serializers.subscriber import SubscriberSerializer
from app.utils.responseutils import send_error_response, send_success_response


# List all subscribers, or create a new subscribers.
# Url: http://<your-domain>/api/v1/subscriber
@api_view(['GET','POST'])
@permission_classes([])
@authentication_classes([])
def subscriber_list(request):
    if request.method == 'GET':
        subscribers = SubscriberModel.objects.filter(company_id=request.company_id)
        serializer = SubscriberSerializer(subscribers, many=True)
        return send_success_response(msg="Subscriber Fetched Successfully", payload=serializer.data)

    elif request.method == 'POST':
        company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(company)
            return send_success_response(msg="Subscriber Added successfully", payload=serializer.data)
        return send_error_response(msg="Subscriber Not Added", payload=serializer.errors)