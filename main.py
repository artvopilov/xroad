from fastapi import FastAPI
from mongoengine import connect

from src.routes import user_router, business_router

connect('test', host='127.0.0.1', port=27017)

app = FastAPI()

app.include_router(users_router)
app.include_router(businesses_router)
