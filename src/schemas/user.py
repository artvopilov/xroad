from mongoengine import Document, StringField, IntField, BooleanField


class User(Document):
    first_name = StringField(required=True)
    middle_name = StringField()
    last_name = StringField()
    username = StringField(required=True)
    password = StringField(required=True)
    image_url = StringField()
    phone = StringField(required=True)
    email = StringField()
    age = IntField(required=True)
    gender_id = IntField(required=True)
    city_id = IntField(required=True)
    is_pro = BooleanField(required=True)
