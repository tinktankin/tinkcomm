from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from app.serializers.signup import SignupSerializer
from app.utils.responseutils import send_error_response, send_success_response


# Signup Company
# Url: http://<your-domain>/api/v1/signup
# Method: POST
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def signup(request):
        serializer =  SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return send_success_response(msg="Company Sign up successfully", payload=serializer.data)
        return send_error_response(msg="Company Signup Failed", payload=serializer.errors)