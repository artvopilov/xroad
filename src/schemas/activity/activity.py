from mongoengine import Document, IntField, StringField, BooleanField, ReferenceField

from src.schemas.user import User


class Activity(Document):
    user_id = ReferenceField(User, required=True)
    name = StringField(required=True)
    description = StringField(required=True)
    x = IntField(required=True)
    y = IntField(required=True)
    is_private = BooleanField(default=False)
    is_active = BooleanField(default=True)
