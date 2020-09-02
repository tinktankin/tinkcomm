from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from app.models.account import  AccountModel
from app.serializers.account import AccountSerializer
from app.utils.stringutils import is_string_empty
from app.utils.responseutils import send_error_response, send_success_response

# Create And List Accounts
# Url: http://<your-domain>/api/v1/accounts/<pk>
# Method: GET
@api_view(['GET', 'POST', ])
@permission_classes([])
@authentication_classes([])
def account_list(request):
    if request.method == 'GET':
        return getAllAccount(request)
    if request.method == 'POST':
        return create(request)


# Get, update and delete account by Id
# Url: http://<your-domain>/api/v1/accounts/<pk>
@api_view(['GET', 'PUT', 'DELETE', ])
@permission_classes([])
@authentication_classes([])
def account_detail(request, pk):

    if request.method == 'GET':
        return getAccount(request, pk)
    if request.method == 'PUT':
        return update(request, pk)
    if request.method == 'DELETE':
        return destroy(request, pk)
    
# Get Account By Id
def getAccount(request, pk=None):
    try:
        account = AccountModel.objects.get(pk=pk)
        serializer = AccountSerializer(account)
        return send_success_response(msg="Account Fetched Successfully", payload=serializer.data)
    except AccountModel.DoesNotExist:
        return send_error_response(msg="Account Not Found", code=status.HTTP_404_NOT_FOUND)


# Get All Account
def getAllAccount(request):
    accounts = AccountModel.objects.filter(company__id=request.company_id)
    serializer = AccountSerializer(accounts, many=True)
    return send_success_response(msg="Accounts Fetched Successfully", payload=serializer.data)



# Create accounts
def create(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(request.company_id)
        return send_success_response(msg="Account created up successfully", payload=serializer.data)
    return send_error_response(msg="Failed to create account", payload=serializer.errors)



# Update accounts
def update(request, pk=None):
    account = get_object(pk)
    if account == None:
        return send_error_response(msg="Account Not Found", code=status.HTTP_404_NOT_FOUND)
    serializer = AccountSerializer(account, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.update()
        return send_success_response(msg="Account updated successfully", payload=serializer.data)
    return send_error_response(msg="Failed to create account", payload=serializer.errors)


# Update accounts
def destroy(request, pk=None):
    account = get_object(pk)
    if account == None:
        return send_error_response(msg="Account Not Found", code=status.HTTP_404_NOT_FOUND)
    account.delete()
    return send_success_response(msg="User account deleted successfully")

# Get Account By PK
def get_object(pk=None):
    try:
        return AccountModel.objects.get(pk=pk)
    except AccountModel.DoesNotExist:
        return None
