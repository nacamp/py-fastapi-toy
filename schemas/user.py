from pydantic import BaseModel, EmailStr

class CreateUserDto(BaseModel):
    name: str
    email: EmailStr
    password: str

class UpdateUserDto(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

class ChangePasswordDto(BaseModel):
    password: str
