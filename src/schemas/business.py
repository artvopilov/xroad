from mongoengine import Document, StringField, ListField


class Business(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    name = StringField(required=True)
    description = StringField()
    logo_url = StringField()
    phone = StringField(required=True)
    email = StringField()
    address = StringField(required=True)
    document_urls = ListField(StringField())
    certificate_urls = ListField(StringField())
