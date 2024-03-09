from fastapi import FastAPI
from mongoengine import connect
from starlette_admin.contrib.mongoengine import Admin, ModelView

from src.routes import user_router, activity_router
from src.schemas import Activity, User

connect('test', host='db', port=27017)

app = FastAPI()

app.include_router(user_router)
app.include_router(activity_router)

admin = Admin()

admin.add_view(ModelView(User))
admin.add_view(ModelView(Activity))

admin.mount_to(app)
