from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers import users
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
