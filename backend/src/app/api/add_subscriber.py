from rest_framework.decorators import api_view, authentication_classes, permission_classes

from app.models.company import CompanyModel
from app.serializers.subscriber import SubscriberSerializer
from app.utils.responseutils import send_error_response, send_success_response


# Add Subscriber Manually
# Url: http://<your-domain>/api/v1/subscriber/add
# Method: POST
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def add_subscriber(request):
        company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(company)
            return send_success_response(msg="Subscriber Added successfully", payload=serializer.data)
        return send_error_response(msg="Not Able to Add Subscriber", payload=serializer.errors)