from fastapi import FastAPI
from mongoengine import connect

from src.routes import user_router, business_router, service_router

connect('test', host='127.0.0.1', port=27017)

app = FastAPI()

app.include_router(user_router)
app.include_router(business_router)
app.include_router(service_router)
