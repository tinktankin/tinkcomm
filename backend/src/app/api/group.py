from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from django.db.models import Q

from app.models.company import CompanyModel
from app.models.group import GroupModel
from app.serializers.group import GroupSerializer
from app.utils.responseutils import send_error_response, send_success_response
from app.utils.pagination import CustomPagination, sorting


# List all groups, or create a new group
# Url: http://<your-domain>/api/v1/groups/
# Method: GET, POST
@api_view(['GET','POST', ])
@permission_classes([])
@authentication_classes([])
def group_list(request):
    if request.method == 'GET':
        return getAll(request)

    if request.method == 'POST':
        return create(request)


# Get, Update or Delete Group By Id
# Url: http://<your-domain>/api/v1/groups/<pk>
# Method: GET, PUT, DELETE
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([])
@authentication_classes([])
def group_detail(request, pk):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    group = get_object(company, pk)
    if group == None:
        return send_error_response(msg="Group Not Found", code=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return get(group)
    if request.method == 'PUT':
        return update(request, group)
    if request.method == 'DELETE':
        return destroy(group)

# Groups bulk delete by Id's
# Url: http://<your-domain>/api/v1/groups/bulk_delete
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def group_bulk_delete(request):

    if request.method == 'POST':
        return bulk_delete(request)

# Get All Group
def getAll(request):
    query = request.GET.get('searchText', '')
    if query:
        text = request.GET['searchText']
        queryset = (Q(name__icontains=text))
        groups = GroupModel.objects.filter(Q(company__id=request.company_id) & queryset)
    else:
        groups = GroupModel.objects.filter(company__id=request.company_id)

    groups = sorting(request, groups)

    paginator = CustomPagination()
    page = paginator.paginate_queryset(groups, request)

    if page is not None:
        serializer = GroupSerializer(page, many=True)
        result = paginator.get_paginated_response(serializer.data)
        data = result.data
    else:
        serializer = GroupSerializer(groups, many=True)
        data = serializer.data

    return send_success_response(msg="Groups Fetched Successfully", payload=data)

# Create Group 
def create(request):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    group = GroupModel(company=company)
    serializer = GroupSerializer(group, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return send_success_response(msg="Group Created successfully", payload=serializer.data)
    return send_error_response(msg="Validation Error", payload=serializer.errors)

# Get group by pk
def get(group):
    serializer = GroupSerializer(group)
    return send_success_response(msg="Group Fetched Successfully", payload=serializer.data)

#Update Group by pk
def update(request, group):
    serializer = GroupSerializer(group, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return send_success_response(msg="Group updated successfully", payload=serializer.data)
    return send_error_response(msg="Validation Error", payload=serializer.errors)

# Delete group
def destroy(group):
    group.delete()
    return send_success_response(msg="Group deleted successfully")

# Get Group By PK
def get_object(company, pk=None):
    try:
        return GroupModel.objects.get(company=company, pk=pk)
    except GroupModel.DoesNotExist:
        return None

# Bulk Delete Groups
def bulk_delete(request):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    ids = request.data['id']
    for id in ids:
        group = get_object(company, id)
        if group is not None:
            group.delete()
    return send_success_response(msg="Groups Deleted successfully")