from fastapi import APIRouter, Depends
from services.auth_service import AuthService
from schemas.auth import LoginDto
from deps.auth import get_auth_service

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(dto: LoginDto, service: AuthService = Depends(get_auth_service)):
    return await service.login(dto)

@router.post("/refresh")
def refresh(body: dict, service: AuthService = Depends(get_auth_service)):
    return service.refresh(body["userId"], body["refreshToken"])

@router.post("/logout")
def logout(body: dict, service: AuthService = Depends(get_auth_service)):
    return service.logout(body["userId"])
