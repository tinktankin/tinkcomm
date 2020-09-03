from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from app.models.company import CompanyModel
from app.models.subscriber import SubscriberModel
from app.serializers.subscriber import SubscriberSerializer
from app.utils.responseutils import send_error_response, send_success_response


# List all subscribers, or create a new subscriber
# Url: http://<your-domain>/api/v1/subscribers/
@api_view(['GET','POST'])
@permission_classes([])
@authentication_classes([])
def subscriber_list(request):

    if request.method == 'GET':
        return getAll(request)
    if request.method == 'POST':
        return create(request)

# Get, Update or Delete Subscriber By Id
# Url: http://<your-domain>/api/v1/subscribers/<pk>
# Method: GET, PUT, DELETE
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([])
@authentication_classes([])
def subscriber_detail(request, pk):

    subscriber = get_object(pk)
    if subscriber == None:
        return send_error_response(msg="Subscriber Not Found", code=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return get(subscriber)
    if request.method == 'PUT':
        return update(request, subscriber)
    if request.method == 'DELETE':
        return destroy(subscriber)

# Get All Subscribers
def getAll(request):
    subscribers = SubscriberModel.objects.filter(company__id=request.company_id)
    serializer = SubscriberSerializer(subscribers, many=True)
    return send_success_response(msg="Subscribers Fetched successfully", payload=serializer.data)

#Create Subscriber
def create(request):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    subscriber = SubscriberModel(company=company)
    serializer = SubscriberSerializer(subscriber, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return send_success_response(msg="Subscriber Created Successfully", payload=serializer.data)
    return send_error_response(msg="Validation Error", payload=serializer.errors)

# Get Subscriber By Id
def get(subscriber):
    serializer = SubscriberSerializer(subscriber)
    return send_success_response(msg="Subscriber Fetched Successfully", payload=serializer.data)

# Update subscriber
def update(request, subscriber):
    serializer = SubscriberSerializer(subscriber, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return send_success_response(msg="subscriber updated successfully", payload=serializer.data)
    return send_error_response(msg="Validation Error", payload=serializer.errors)

# Delete subscriber
def destroy(subscriber):
    subscriber.delete()
    return send_success_response(msg="Subscriber deleted successfully")

#Get Subscriber by pk
def get_object(pk=None):
    try:
        return SubscriberModel.objects.get(pk=pk)
    except SubscriberModel.DoesNotExist:
        return None



