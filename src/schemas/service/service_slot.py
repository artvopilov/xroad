from mongoengine import Document, IntField, ReferenceField, DateField, FloatField

from src.schemas.service.service import Service


class ServiceSlot(Document):
    service = ReferenceField(Service, required=True)
    start_date_time = DateField(required=True)
    end_date_time = DateField(required=True)
    price = FloatField()
    max_users = IntField()
