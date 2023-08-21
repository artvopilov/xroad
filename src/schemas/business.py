from mongoengine import StringField, ListField, Document


class Business(Document):
    name = StringField(required=True)
    description = StringField()
    address = StringField(required=True)
    image_url = StringField()
    document_urls = ListField(StringField())
    certificate_urls = ListField(StringField())
