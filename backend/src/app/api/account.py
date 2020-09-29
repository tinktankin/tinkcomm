from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from app.models.account import  AccountModel
from app.serializers.account import AccountSerializer
from app.serializers.company import CompanyModel
from app.utils.stringutils import is_string_empty
from app.utils.responseutils import send_error_response, send_success_response
from app.utils.pagination import CustomPagination

# Create And List Accounts
# Url: http://<your-domain>/api/v1/accounts/
# Method: GET
@api_view(['GET', 'POST', ])
@permission_classes([])
@authentication_classes([])
def account_list(request):
    if request.method == 'GET':
        return getAll(request)
    if request.method == 'POST':
        return create(request)


# Get, update and delete account by Id
# Url: http://<your-domain>/api/v1/accounts/<pk>
@api_view(['GET', 'PUT', 'DELETE', ])
@permission_classes([])
@authentication_classes([])
def account_detail(request, pk):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    account = get_object(company, pk)
    if account == None:
        return send_error_response(msg="Account Not Found", code=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return get(account)
    if request.method == 'PUT':
        return update(request, account)
    if request.method == 'DELETE':
        return destroy(account)

# Accounts bulk delete by Id's
# Url: http://<your-domain>/api/v1/accounts/bulk_delete
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def account_bulk_delete(request):

    if request.method == 'POST':
        return bulk_delete(request)
    
# Get Account By Id
def get(account):
    serializer = AccountSerializer(account)
    return send_success_response(msg="Account Fetched Successfully", payload=serializer.data)


# Get All Account
def getAll(request):
    paginator = CustomPagination()
    accounts = AccountModel.objects.filter(company__id=request.company_id)
    page = paginator.paginate_queryset(accounts, request)

    if page is not None:
        serializer = AccountSerializer(page, many=True)
        result = paginator.get_paginated_response(serializer.data)
        data = result.data
    else:
        serializer = AccountSerializer(accounts, many=True)
        data = serializer.data

    return send_success_response(msg="Accounts Fetched Successfully", payload=data)


# Create accounts
def create(request):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    account = AccountModel(company=company)
    serializer = AccountSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return send_success_response(msg="Account created up successfully", payload=serializer.data)
    return send_error_response(msg="Validation Errors", payload=serializer.errors)



# Update accounts
def update(request, account):
    serializer = AccountSerializer(account, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return send_success_response(msg="Account updated successfully", payload=serializer.data)
    return send_error_response(msg="Validation Error", payload=serializer.errors)


# Delete accounts
def destroy(account):
    account.delete()
    return send_success_response(msg="User account deleted successfully")

# Get Account By PK
def get_object(company, pk=None):
    try:
        return AccountModel.objects.get(company=company, pk=pk)
    except AccountModel.DoesNotExist:
        return None

# Bulk Delete Accounts
def bulk_delete(request):
    company = CompanyModel.objects.get(id=request.company_id, status='ACTIVE')
    ids = request.data['id']
    for id in ids:
        account = get_object(company, id)
        if account is not None:
            account.delete()
    return send_success_response(msg="Accounts Deleted successfully")
