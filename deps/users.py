from fastapi import Depends
from sqlalchemy.orm import Session
from db.session import get_session
from services.users_service import UsersService


CONFIG = {"dbHost": "localhost", "dbPort": 5432}  # 임시 config


def get_users_service(session: Session = Depends(get_session)):
    return UsersService(session, CONFIG)