from mongoengine import Document, StringField, IntField, BooleanField, ListField, EmailField


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
    age = IntField()
    gender = StringField(choices=['male', 'female'])
    city = StringField()
    is_pro = BooleanField()

    # business
    description = StringField()
    address = StringField()
    document_urls = ListField(StringField(), default=None)
    certificate_urls = ListField(StringField(), default=None)
