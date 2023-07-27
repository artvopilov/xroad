from mongoengine import Document, IntField, DateField, FloatField, ObjectIdField


class ServiceSlot(Document):
    service_id = ObjectIdField(required=True)
    start_date_time = DateField(required=True)
    end_date_time = DateField(required=True)
    price = FloatField()
    max_users = IntField()
