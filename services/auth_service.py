from utils.jwt import create_access_token, create_refresh_token, decode_token
from schemas.auth import LoginDto, TokenResponse
import bcrypt
from services.users_service import UsersService

class AuthService:
    def __init__(self, users_service: UsersService):
        self.users_service = users_service
        # 메모리 저장 (user_id → refresh_token)
        self.refresh_tokens: dict[str, str] = {}

    async def login(self, dto: LoginDto) -> TokenResponse:
        email, password = dto.email, dto.password

        # 유저 조회
        user = self.users_service.find_user_by_email(email)
        if not user:
            return {"message": "User not found"}

        # 비밀번호 검증
        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            return {"message": "Invalid credentials"}

        # JWT payload
        payload = {"email": user.email, "sub": user.id}

        # 토큰 발급
        access_token = create_access_token(payload)
        refresh_token = create_refresh_token(payload)
        self.refresh_tokens[user.id] = refresh_token
        
        return {"data": TokenResponse(access_token=access_token, refresh_token=refresh_token)}

    def refresh(self, user_id: str, refresh_token: str) -> TokenResponse:
        decoded = decode_token(refresh_token)
        if decoded["sub"] != user_id:
            raise Exception("Invalid refresh token")
        return {"data": TokenResponse(
            access_token=create_access_token(user_id),
            refresh_token=create_refresh_token(user_id)
        )}

    def logout(self, user_id: str):
        # 실무에서는 refreshToken 블랙리스트 처리
        return {"message": f"User {user_id} logged out (no-op)"}
