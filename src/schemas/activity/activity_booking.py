from mongoengine import Document, ReferenceField, BooleanField

from src.schemas.activity.activity_slot import ActivitySlot
from src.schemas.user import User


class ActivityBooking(Document):
    slot = ReferenceField(ActivitySlot, required=True)
    user = ReferenceField(User, required=True)
    is_accepted = BooleanField(default=False)
