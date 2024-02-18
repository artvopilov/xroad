from mongoengine import Document, StringField, BooleanField, ListField, DateField


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    user_type = StringField(required=True, choices=['person', 'business'])
    phone = StringField(required=True)
    email = StringField()
    image_url = StringField()

    # person
    person_first_name = StringField()
    person_middle_name = StringField()
    person_last_name = StringField()
    person_date_of_birth = DateField()
    person_gender = StringField(choices=['male', 'female'])
    person_is_pro = BooleanField()

    # business
    business_registration_id = StringField()
    business_name = StringField()
    business_description = StringField()
    business_address = StringField()
    business_certificate_urls = ListField(StringField(), default=None)
    business_is_verified = BooleanField()
