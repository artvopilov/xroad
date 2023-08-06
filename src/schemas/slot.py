from mongoengine import Document, IntField, DateTimeField, FloatField, ObjectIdField


class Slot(Document):
    activity_id = ObjectIdField(required=True)
    start_date_time = DateTimeField(required=True)
    end_date_time = DateTimeField(required=True)
    price = FloatField()
    max_users = IntField()
