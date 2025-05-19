from sqlmodel import Session, select
from models.user import User
from schemas.user import CreateUserDto, UpdateUserDto
import bcrypt
import logging

logger = logging.getLogger("app")

class UsersService:
    def __init__(self, session: Session, config: dict):
        self.session = session
        self.config = config

    def create(self, dto: CreateUserDto):
        hashed_pw = bcrypt.hashpw(dto.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(name=dto.name, email=dto.email, password=hashed_pw)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def find_all(self):
        logger.info(f"Config: {self.config}")
        return self.session.exec(select(User)).all()

    def find_one(self, id: int):
        return self.session.get(User, id)

    def update(self, id: int, dto: UpdateUserDto):
        user = self.session.get(User, id)
        if not user:
            return None
        for field, value in dto.model_dump(exclude_unset=True).items():
            setattr(user, field, value)
        self.session.add(user)
        self.session.commit()
        return user

    def remove(self, id: int):
        user = self.session.get(User, id)
        if not user:
            return None
        self.session.delete(user)
        self.session.commit()
        return {"deleted": id}

    def change_password(self, id: int, new_password: str):
        user = self.session.get(User, id)
        if not user:
            return None
        user.password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        self.session.add(user)
        self.session.commit()
        return {"password_changed": True}

    def find_user_by_email(self, email: str):
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()
