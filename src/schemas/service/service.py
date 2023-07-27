from mongoengine import Document, IntField, StringField, BooleanField, ObjectIdField


class Service(Document):
    business_id = ObjectIdField(required=True)
    name = StringField(required=True)
    description = StringField(required=True)
    x = IntField(required=True)
    y = IntField(required=True)
    is_private = BooleanField(default=False)
    is_active = BooleanField(default=True)
