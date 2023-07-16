from mongoengine import Document, ReferenceField, BooleanField

from src.schemas.service.service_slot import ServiceSlot
from src.schemas.user import User


class ServiceBooking(Document):
    slot = ReferenceField(ServiceSlot, required=True)
    user = ReferenceField(User, required=True)
    is_accepted = BooleanField(default=False)
    is_paid = BooleanField(default=False)
