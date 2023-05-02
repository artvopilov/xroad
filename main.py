from fastapi import FastAPI

from src.routes import users

app = FastAPI()

app.include_router(users.router)
