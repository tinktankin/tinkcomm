from rest_framework.decorators import api_view, authentication_classes, permission_classes

from app.models.company import CompanyModel
from app.models.group import GroupModel
from app.serializers.group import GroupSerializer
from app.utils.responseutils import send_error_response, send_success_response


# Create Group
# Url: http://<your-domain>/api/v1/group
# Method: POST
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def create_group(request):
        company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
        group = GroupModel(company=company)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return send_success_response(msg="Group Added successfully", payload=serializer.data)
        return send_error_response(msg="Not Able to Add Group", payload=serializer.errors)