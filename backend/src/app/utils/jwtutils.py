from datetime import datetime, timedelta
import jwt

JWT_SECRET = 'bA2xcjpf8y5aSUFsNB2qN5yymUBSs6es3qHoFpGkec75RCeBb8cpKauGefw5qy4'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_DAYS = 1

def create_token(payload):
    
    payload['exp'] = datetime.utcnow() + timedelta(days=JWT_EXP_DELTA_DAYS)
    jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return jwt_token

def decode_token(jwt_token):
    try:
        payload = jwt.decode(jwt_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        return None 
    



