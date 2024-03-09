from fastapi import FastAPI
from mongoengine import connect

from src.routes import user_router, activity_router

connect('test', host='db', port=27017)

app = FastAPI()

app.include_router(user_router)
app.include_router(activity_router)
