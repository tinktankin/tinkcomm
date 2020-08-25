from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response

from app.models.account import  AccountModel
from app.serializers.account import AccountSerializer
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


# Get All Company
# Url: http://<your-domain>/api/v1/account
# Method: GET
@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def get_all_account(request):
    accounts = AccountModel.objects.filter(company__id=request.company_id)
    serializer = AccountSerializer(accounts, many = True)
    return send_success_response(msg="Accounts Fetched Successfully", payload=serializer.data)
