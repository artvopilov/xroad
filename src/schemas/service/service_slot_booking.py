from mongoengine import Document, BooleanField, ObjectIdField


class ServiceSlotBooking(Document):
    slot_id = ObjectIdField(required=True)
    user_id = ObjectIdField(required=True)
    is_accepted = BooleanField(default=False)
    is_paid = BooleanField(default=False)
