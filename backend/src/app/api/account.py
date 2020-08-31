from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response

from app.models.account import  AccountModel
from app.serializers.account import AccountSerializer, UpdateAccountSerializer
from app.utils.stringutils import is_string_empty
from app.utils.responseutils import send_error_response, send_success_response

# Get Account By Id
# Url: http://<your-domain>/api/v1/account/<pk>
# Method: GET
@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def get_account(request, pk):
    try:
        account = AccountModel.objects.get(pk=pk)
        serializer = AccountSerializer(account)
        return send_success_response(msg="Account Fetched Successfully", payload=serializer.data)
    except AccountModel.DoesNotExist:
        return send_error_response(msg="Account Not Found", code=status.HTTP_404_NOT_FOUND)


# CRUD operations for accounts
# Url: http://<your-domain>/api/v1/account
# Method: GET, POST, PUT, DELETE
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([])
@authentication_classes([])
def account_list(request):
    user_id = request.user_id
    company_id = request.company_id

    if request.method == 'GET':
        accounts = AccountModel.objects.filter(company__id=company_id)
        serializer = AccountSerializer(accounts, many=True)
        return send_success_response(msg="Accounts Fetched Successfully", payload=serializer.data)

    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(company_id)
            return send_success_response(msg="User signed up successfully", payload=serializer.data)
        return send_error_response(msg="User Signup Failed", payload=serializer.errors)

    elif request.method == 'PUT':
        serializer = UpdateAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(user_id)
            return send_success_response(msg="User account updated successfully", payload=serializer.data)
        return send_error_response(msg="User account could not be updated", payload=serializer.errors)

    elif request.method == 'DELETE':
        account = AccountModel.objects.filter(id=user_id)
        account.update(status='INACTIVE')
        return send_success_response(msg="User account deleted successfully")

"""
# Create account
# Url: http://<your-domain>/api/v1/account/signup
# Method: POST
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def signup_account(request):
    company_id = request.company_id

    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(company_id)
        return send_success_response(msg="User signed up successfully", payload=serializer.data)
    return send_error_response(msg="User Signup Failed", payload=serializer.errors)


# Update account
# Url: http://<your-domain>/api/v1/account/update
# Method: POST
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def update_account(request):
    user_id = request.user_id

    serializer = UpdateAccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.update(user_id)
        return send_success_response(msg="User account updated successfully", payload=serializer.data)
    return send_error_response(msg="User account could not be updated", payload=serializer.errors)


# Delete account
# Url: http://<your-domain>/api/v1/account/delete
# Method: POST
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def delete_account(request):
    user_id = request.user_id

    account = AccountModel.objects.filter(id=user_id)
    account.update(status='INACTIVE')
    return send_success_response(msg="User account deleted successfully")
"""