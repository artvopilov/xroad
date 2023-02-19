from mongoengine import Document, DateTimeField, IntField, StringField


class Event(Document):
    name = StringField()
    x = IntField()
    y = IntField()
    start = DateTimeField()
    end = DateTimeField()
