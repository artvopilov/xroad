from mongoengine import Document, StringField, IntField, BooleanField, ListField


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    user_type = StringField(required=True, choices=['person', 'business'])

    # common
    name = StringField(required=True)
    phone = StringField(required=True)
    email = StringField()
    image_url = StringField()

    # person
    middle_name = StringField()
    last_name = StringField()
    age = IntField(required=True)
    gender = StringField(required=True)
    city = StringField(required=True)
    is_pro = BooleanField(default=False)

    # business
    description = StringField()
    address = StringField(required=True)
    document_urls = ListField(StringField())
    certificate_urls = ListField(StringField())

