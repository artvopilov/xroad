from mongoengine import Document, IntField, DateField, ObjectIdField


class ActivitySlot(Document):
    activity_id = ObjectIdField(required=True)
    start_date_time = DateField(required=True)
    end_date_time = DateField(required=True)
    max_users = IntField()
