from fastapi import APIRouter, Depends
from db.session import get_session
from services.users_service import UsersService
from schemas.user import CreateUserDto, UpdateUserDto, ChangePasswordDto
from sqlmodel import Session

router = APIRouter(prefix="/users", tags=["users"])

CONFIG = {"dbHost": "localhost", "dbPort": 5432}  # 임시 config

def get_service(session: Session = Depends(get_session)):
    return UsersService(session, CONFIG)

@router.post("/")
def create_user(dto: CreateUserDto, service: UsersService = Depends(get_service)):
    return service.create(dto)

@router.get("/")
def get_all(service: UsersService = Depends(get_service)):
    return service.find_all()

@router.get("/{id}")
def get_user(id: int, service: UsersService = Depends(get_service)):
    return service.find_one(id)

@router.patch("/{id}")
def update_user(id: int, dto: UpdateUserDto, service: UsersService = Depends(get_service)):
    return service.update(id, dto)

@router.delete("/{id}")
def delete_user(id: int, service: UsersService = Depends(get_service)):
    return service.remove(id)

@router.patch("/{id}/password")
def change_password(id: int, dto: ChangePasswordDto, service: UsersService = Depends(get_service)):
    return service.change_password(id, dto.password)
