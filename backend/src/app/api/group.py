from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from app.models.company import CompanyModel
from app.models.group import GroupModel
from app.serializers.group import GroupSerializer
from app.utils.responseutils import send_error_response, send_success_response


# List all groups, or create a new group
# Url: http://<your-domain>/api/v1/group/
# Method: GET, POST
@api_view(['GET','POST', ])
@permission_classes([])
@authentication_classes([])
def group_list(request):
    if request.method == 'GET':
        groups = GroupModel.objects.filter(company_id=request.company_id)
        serializer = GroupSerializer(groups, many=True)
        return send_success_response(msg="Groups Found", payload=serializer.data)

    elif request.method == 'POST':
        company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
        group = GroupModel(company=company)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return send_success_response(msg="Group Created successfully", payload=serializer.data)
        return send_error_response(msg="Unable To Add Group", payload=serializer.errors)


# Get, Update or Delete Group By Id
# Url: http://<your-domain>/api/v1/group/<pk>
# Method: GET, PUT, DELETE
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([])
@authentication_classes([])
def group_detail(request, pk):
    try:
        group = GroupModel.objects.get(pk=pk)
    except GroupModel.DoesNotExist:
        return send_error_response(msg="Group Not Found", code=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return send_success_response(msg="Group Found", payload=serializer.data)

    elif request.method == 'PUT':
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return send_success_response(msg="Group Details Updated Successfully", payload=serializer.data)
        return send_error_response(msg="Unable To Update Group Details", payload=serializer.errors)

    elif request.method == 'DELETE':
        operation = group.delete()
        if operation:
            return send_success_response(msg="Group Deleted Successfully")
        else:
            return send_error_response(msg="Unable To Delete Group")