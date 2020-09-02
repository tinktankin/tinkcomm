from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response

from app.utils.responseutils import send_error_response, send_success_response
from app.utils.stringutils import is_string_empty
from app.models.account import AccountModel
from app.models.company import CompanyModel
from app.utils.jwtutils import create_token

# Signin User
# Url: http://<your-domain>/api/v1/login
# Method: POST
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def login(request):
    
    company_code = request.data.get('company_code', '')
    if is_string_empty(company_code):
        return send_error_response('company_code filed is required')

    email = request.data.get('email', '')
    if is_string_empty(email):
        return send_error_response('email filed is required.')

    password = request.data.get('password', '')
    if is_string_empty(password):
        return send_error_response('password field required.')
    
    try:
        company = CompanyModel.objects.get(code=company_code, status='ACTIVE')
        account = AccountModel.objects.get(email=email, password=password, status='ACTIVE', company=company)
    except CompanyModel.DoesNotExist:
        return send_error_response('Invalid Company Code')
    except AccountModel.DoesNotExist:
        return send_error_response('Invalid Email or Password')
    
    jwt_token = create_token({'company_id': company.id, 'user_id': account.id})
    return send_success_response("Login Successful", {'token':jwt_token})

# Sign Out User
# Url: http://<your-domain>/api/v1/logout
# Method: POST
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def logout(request):
    
    return send_success_response(msg="Logout Successfully", payload={})
        
    

