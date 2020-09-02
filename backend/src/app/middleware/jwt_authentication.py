from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse

from app.utils.jwtutils import decode_token
from config.settings import PUBLIC_URLS

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            PUBLIC_URLS.index(request.path)
            return self.get_response(request)
        except ValueError:
            pass
        
        jwt_token = request.headers.get('authorization', None)
        if jwt_token == None :
            return self.unauthorized_response("Missing Token")
        try:
            jwt_token = jwt_token.split("Bearer ")[1]
        except Exception:
            return self.unauthorized_response('Invalid Token')
        payload  = decode_token(jwt_token)
        if payload == None: 
            return self.unauthorized_response('Invalid Token')
    
        request.user_id = payload['user_id']
        request.company_id = payload['company_id']
        response = self.get_response(request)
        return response

    def unauthorized_response(self, error_msg):
        response = HttpResponse(error_msg)
        response.status_code = 401
        return response