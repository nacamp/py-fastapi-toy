from utils.jwt import create_access_token, create_refresh_token, decode_token
from schemas.auth import LoginDto, TokenResponse
import bcrypt

# 더미 유저 DB
fake_user = {
    "id": "user123",
    "email": "test@example.com",
    "password": bcrypt.hashpw("password".encode(), bcrypt.gensalt()).decode()
}


class AuthService:
    def login(self, dto: LoginDto) -> TokenResponse:
        # if dto.email != fake_user["email"]:
        #     raise Exception("User not found")
        # if not bcrypt.checkpw(dto.password.encode(), fake_user["password"].encode()):
        #     raise Exception("Invalid password")

        access = create_access_token(fake_user["id"])
        refresh = create_refresh_token(fake_user["id"])
        return {"data": TokenResponse(access_token=access, refresh_token=refresh)}
        # return TokenResponse(access_token=access, refresh_token=refresh)

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
