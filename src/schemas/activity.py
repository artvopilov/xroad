from mongoengine import Document, FloatField, StringField, BooleanField, ObjectIdField, DateField, DictField


class Activity(Document):
    user_id = ObjectIdField(required=True)
    name = StringField(required=True)
    description = StringField()
    conditions = StringField()
    x = FloatField(required=True)
    y = FloatField(required=True)
    schedule = DictField()
    period_start = DateField()
    period_end = DateField()
    is_private = BooleanField(default=False)
    is_active = BooleanField(default=True)
