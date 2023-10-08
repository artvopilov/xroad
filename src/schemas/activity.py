from mongoengine import Document, IntField, StringField, BooleanField, ObjectIdField


class Activity(Document):
    user_id = ObjectIdField(required=True)
    name = StringField(required=True)
    description = StringField()
    x = IntField(required=True)
    y = IntField(required=True)
    is_private = BooleanField(default=False)
    is_active = BooleanField(default=True)
