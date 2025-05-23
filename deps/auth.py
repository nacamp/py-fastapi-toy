from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt import decode_token  # PyJWT 기반
from services.auth_service import AuthService
from services.users_service import UsersService
from deps.users import get_users_service

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        token = credentials.credentials
        payload = decode_token(token)
        print('get_current_user', payload)
        return payload["sub"]  # 또는 유저 객체 조회
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_auth_service(users_service: UsersService = Depends(get_users_service)):
    return AuthService(users_service)
