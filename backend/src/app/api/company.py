from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response

from app.models.company import  CompanyModel
from app.models.account import  AccountModel
from app.serializers.company import CompanySerializer
from app.serializers.account import AccountSerializer
from app.utils.stringutils import is_string_empty
from app.utils.responseutils import send_error_response, send_success_response

# Get Company By Id
# Url: http://<your-domain>/api/v1/company/<pk>
# Method: GET
@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def get_company(request, pk):
    try:
        company = CompanyModel.objects.get(pk=pk)
        serializer = CompanySerializer(company)
        return send_success_response(msg="Company Fetched Successfully", payload=serializer.data)
    except CompanyModel.DoesNotExist:
        return send_error_response(msg="Company Not Found", code=status.HTTP_404_NOT_FOUND)


# Get All Company
# Url: http://<your-domain>/api/v1/company
# Method: GET
@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def get_all_company(request):
    companies = CompanyModel.objects.all()
    serializer = CompanySerializer(companies, many = True)
    return send_success_response(msg="Companies Fetched Successfully", payload=serializer.data)
