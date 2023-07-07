from mongoengine import Document, StringField, ListField


class Business(Document):
    name: StringField(required=True)
    address: StringField(required=True)
    document_urls: ListField()
    username: StringField(required=True)
    password: StringField(required=True)
    image_url: StringField()
    phone: StringField(required=True)
    email: StringField()
    description: StringField()
    certificate_urls: ListField()
