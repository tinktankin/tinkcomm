from rest_framework.decorators import api_view, authentication_classes, permission_classes

from app.models.subscriber import SubscriberModel
from app.serializers.subscriber import SubscriberSerializer
from app.utils.responseutils import send_error_response, send_success_response

# Get All Subscriber By Company Id
# Url: http://<your-domain>/api/v1/subscriber/
# Method: GET
@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def get_all_subscriber(request):
    subscribers = SubscriberModel.objects.filter(company_id=request.company_id)
    serializer = SubscriberSerializer(subscribers, many=True)
    return send_success_response(msg="Subscriber Fetched Successfully", payload=serializer.data)