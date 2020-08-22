from rest_framework.response import Response

def send_error_response(msg='Error', code=400, payload={}):
    data = {}
    data['success'] = False
    data['message'] = msg
    data['error_code'] = code
    data['data'] = payload
    return Response(data, status=code)

def send_success_response(msg='Success', payload={}, code=200):
    data = {}
    data['success'] = True
    data['message'] = msg
    data['data'] = payload
    return Response(data, status=code)
