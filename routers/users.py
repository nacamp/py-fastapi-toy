from fastapi import APIRouter, Body, Path, Request

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/")
def create_user(create_user_dto: dict = Body(...)):
    return {"message": "User created (dummy)", "data": create_user_dto}

@router.get("/")
def find_all_users(request: Request):
    # request.state.user 등에서 인증된 사용자 정보 접근 가능 (미구현 상태)
    return {"message": "All users (dummy)"}

@router.get("/{id}")
def find_one_user(id: str = Path(...)):
    return {"message": "User detail (dummy)", "id": id}

@router.patch("/{id}")
def update_user(id: str, update_user_dto: dict = Body(...)):
    return {"message": "User updated (dummy)", "id": id, "data": update_user_dto}

@router.delete("/{id}")
def remove_user(id: str):
    return {"message": "User deleted (dummy)", "id": id}

@router.patch("/{id}/password")
def change_password(id: str, body: dict = Body(...)):
    return {"message": "Password changed (dummy)", "id": id, "new_password": body.get("password")}
