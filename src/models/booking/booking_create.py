from pydantic import BaseModel


class BookingCreate(BaseModel):
    slot_id: str
