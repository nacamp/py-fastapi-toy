from pydantic import BaseModel

class LoginDto(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    id: str
    access_token: str
    refresh_token: str
