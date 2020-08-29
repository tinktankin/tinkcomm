from rest_framework.decorators import api_view, authentication_classes, permission_classes

from app.serializers.group import GroupSerializer
from app.utils.responseutils import send_error_response, send_success_response


# Create Group
# Url: http://<your-domain>/api/v1/group/create
# Method: POST
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def create_group(request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return send_success_response(msg="Group Added successfully", payload=serializer.data)
        return send_error_response(msg="Not Able to Add Group", payload=serializer.errors)