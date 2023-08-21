from mongoengine import Document, StringField


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    user_type = StringField(required=True)
    phone = StringField(required=True)
    email = StringField()
