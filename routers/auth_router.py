from fastapi import APIRouter, Depends
from services.auth_service import AuthService
from schemas.auth import LoginDto

router = APIRouter(prefix="/auth", tags=["auth"])
auth_service = AuthService()  # DI 대신 직접 생성

@router.post("/login")
def login(dto: LoginDto):
    return auth_service.login(dto)

@router.post("/refresh")
def refresh(body: dict):
    return auth_service.refresh(body["userId"], body["refreshToken"])

@router.post("/logout")
def logout(body: dict):
    return auth_service.logout(body["userId"])
