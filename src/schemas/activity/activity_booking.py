from mongoengine import Document, BooleanField, ObjectIdField


class ActivityBooking(Document):
    slot_id = ObjectIdField(required=True)
    user_id = ObjectIdField(required=True)
    is_accepted = BooleanField(default=False)
