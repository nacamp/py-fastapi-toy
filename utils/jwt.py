import jwt
from datetime import datetime, timedelta
from typing import Dict

SECRET_KEY = "my-secret"
ALGORITHM = "HS256"


def create_token(payload: Dict, expires_delta: timedelta) -> str:
    to_encode = payload.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode["exp"] = int(expire.timestamp()) 
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_access_token(payload: Dict) -> str:
    return create_token(payload, timedelta(days=7))

def create_refresh_token(payload: Dict) -> str:
    return create_token(payload, timedelta(days=7))

# def create_access_token(user_id: str, expires_delta: int = 15):
#     expire = datetime.utcnow() + timedelta(minutes=expires_delta)
#     to_encode = {
#         "sub": user_id,
#         "exp": expire
#     }
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# def create_refresh_token(payload: Dict) -> str:
#     return create_token(payload, timedelta(days=7))

# # def create_refresh_token(user_id: str, expires_delta: int = 60 * 24 * 7):
# #     expire = datetime.utcnow() + timedelta(minutes=expires_delta)
# #     to_encode = {
# #         "sub": user_id,
# #         "exp": expire
# #     }
# #     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
