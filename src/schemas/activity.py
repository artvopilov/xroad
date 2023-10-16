from mongoengine import Document, FloatField, StringField, BooleanField, ObjectIdField


class Activity(Document):
    user_id = ObjectIdField(required=True)
    name = StringField(required=True)
    description = StringField()
    x = FloatField(required=True)
    y = FloatField(required=True)
    is_private = BooleanField(default=False)
    is_active = BooleanField(default=True)
