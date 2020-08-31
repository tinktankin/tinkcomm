from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from app.models.company import CompanyModel
from app.models.subscriber import SubscriberModel
from app.serializers.subscriber import SubscriberSerializer
from app.utils.responseutils import send_error_response, send_success_response


# List all subscribers, or create a new subscriber
# Url: http://<your-domain>/api/v1/subscriber/
@api_view(['GET','POST'])
@permission_classes([])
@authentication_classes([])
def subscriber_list(request):
    if request.method == 'GET':
        subscribers = SubscriberModel.objects.filter(company_id=request.company_id)
        serializer = SubscriberSerializer(subscribers, many=True)
        return send_success_response(msg="Subscribers Found", payload=serializer.data)

    elif request.method == 'POST':
        company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
        subscriber = SubscriberModel(company=company)
        serializer = SubscriberSerializer(subscriber, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return send_success_response(msg="Subscriber Created Successfully", payload=serializer.data)
        return send_error_response(msg="Unable To Add Subscriber", payload=serializer.errors)


# Get, Update or Delete Subscriber By Id
# Url: http://<your-domain>/api/v1/subscriber/<pk>
# Method: GET, PUT, DELETE
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([])
@authentication_classes([])
def subscriber_detail(request, pk):
    try:
        subscriber = SubscriberModel.objects.get(pk=pk)
    except SubscriberModel.DoesNotExist:
        return send_error_response(msg="Subscriber Not Found", code=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubscriberSerializer(subscriber)
        return send_success_response(msg="Subscriber Found", payload=serializer.data)

    elif request.method == 'PUT':
        serializer = SubscriberSerializer(subscriber, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return send_success_response(msg="Subscriber Details Updated Successfully", payload=serializer.data)
        return send_error_response(msg="Unable To Update Subscriber Details", payload=serializer.errors)

    elif request.method == 'DELETE':
        operation = subscriber.delete()
        if operation:
            return send_success_response(msg="Subscriber Deleted Successfully")
        else:
            return send_error_response(msg="Unable To Delete Subscriber")

