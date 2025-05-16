from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers import users, auth_router, public_users_router
from db.session import engine
from models.user import SQLModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    SQLModel.metadata.create_all(engine)
    yield
    print("Shutdown")

app = FastAPI(lifespan=lifespan)
app.include_router(users.router)
app.include_router(public_users_router.router)
app.include_router(auth_router.router)