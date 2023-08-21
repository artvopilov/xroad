from mongoengine import StringField, IntField, BooleanField, Document


class Person(Document):
    first_name = StringField(required=True)
    middle_name = StringField()
    last_name = StringField()
    age = IntField(required=True)
    gender = StringField(required=True)
    city = StringField(required=True)
    image_url = StringField()
    is_pro = BooleanField(required=True, default=False)
