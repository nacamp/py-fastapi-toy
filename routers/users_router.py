from fastapi import APIRouter, Depends, Path
from db.session import get_session
from services.users_service import UsersService
from schemas.user import CreateUserDto, UpdateUserDto, ChangePasswordDto
from sqlmodel import Session
from typing import Annotated
from deps.auth import get_current_user
from deps.users import get_users_service

router = APIRouter(
    prefix="/users", tags=["users"], dependencies=[Depends(get_current_user)])

@router.get("/")
def get_all(service: UsersService = Depends(get_users_service)):
    return service.find_all()


@router.get("/{id}")
def get_user(
    id: Annotated[int, Path(..., description="user id")],
    service: Annotated[UsersService, Depends(get_users_service)] = ...
):
    return service.find_one(id)


@router.patch("/{id}")
def update_user(id: int, dto: UpdateUserDto, service: UsersService = Depends(get_users_service)):
    return service.update(id, dto)


@router.delete("/{id}")
def delete_user(id: int, service: UsersService = Depends(get_users_service)):
    return service.remove(id)


@router.patch("/{id}/password")
def change_password(id: int, dto: ChangePasswordDto, service: UsersService = Depends(get_users_service)):
    return service.change_password(id, dto.password)
