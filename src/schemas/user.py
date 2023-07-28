from mongoengine import Document, StringField, IntField, BooleanField


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    first_name = StringField(required=True)
    middle_name = StringField()
    last_name = StringField()
    photo_url = StringField()
    age = IntField(required=True)
    gender_id = IntField(required=True)
    city_id = IntField(required=True)
    phone = StringField(required=True)
    email = StringField()
    is_pro = BooleanField(required=True, default=False)
