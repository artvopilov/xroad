from mongoengine import Document, StringField, IntField


class User(Document):
    username = StringField()
    password = StringField()
    name = StringField()
    age = IntField()
    type = StringField()
