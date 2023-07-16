from mongoengine import Document, IntField, ReferenceField, DateField

from src.schemas.activity.activity import Activity


class ActivitySlot(Document):
    activity = ReferenceField(Activity, required=True)
    start_date_time = DateField(required=True)
    end_date_time = DateField(required=True)
    max_users = IntField()
