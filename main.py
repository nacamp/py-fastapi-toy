from fastapi import FastAPI
from routers import users
from db.session import engine
from models.user import SQLModel

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(users.router)
