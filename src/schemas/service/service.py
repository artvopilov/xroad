from mongoengine import Document, IntField, StringField, BooleanField, ReferenceField

from src.schemas.business import Business


class Service(Document):
    business = ReferenceField(Business, required=True)
    name = StringField(required=True)
    description = StringField(required=True)
    x = IntField(required=True)
    y = IntField(required=True)
    is_private = BooleanField(default=False)
    is_active = BooleanField(default=True)
