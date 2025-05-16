from fastapi import APIRouter, Depends, Path
from db.session import get_session
from services.users_service import UsersService
from schemas.user import CreateUserDto, UpdateUserDto, ChangePasswordDto
from sqlmodel import Session
from typing import Annotated

router = APIRouter(prefix="/users", tags=["users"])

CONFIG = {"dbHost": "localhost", "dbPort": 5432}  # 임시 config


def get_service(session: Session = Depends(get_session)):
    return UsersService(session, CONFIG)


@router.post("/")
def create_user(dto: CreateUserDto, service: UsersService = Depends(get_service)):
    return service.create(dto)
