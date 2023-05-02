from fastapi import FastAPI
from mongoengine import connect

from src.routes import users

connect('test', host='127.0.0.1', port=27017)

app = FastAPI()

app.include_router(users.router)
