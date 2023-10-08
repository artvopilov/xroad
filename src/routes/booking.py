from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from src.models import Booking as BookingModel
from src.route_deps import RouteDeps
from src.schemas import User as UserSchema, Slot as SlotSchema, Booking as BookingSchema

router = APIRouter(prefix='/bookings', tags=['bookings'])


@router.post('/{slot_id}/booking', response_model=BookingModel)
async def create_booking(
    slot_id: str,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    slot_schema = SlotSchema.objects(id=slot_id).first()
    if slot_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No slot with this id')
    if user_schema.user_type == 'business':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not allowed for business')
    booking_schema = BookingSchema(slot_id=slot_schema.id, user_id=user_schema.id).save()
    return booking_schema.to_mongo()


@router.get('', response_model=list[BookingModel])
async def get_bookings(slot_id: str = None, user_id: str = None, skip: int = 0, limit: int = 10):
    booking_schemas = BookingSchema.objects()
    if slot_id is not None:
        booking_schemas = booking_schemas.objects(slot_id=slot_id)
    if user_id is not None:
        booking_schemas = booking_schemas.objects(user_id=user_id)
    booking_schemas = booking_schemas[skip: limit]
    return list(booking_schemas.as_pymongo())


@router.get('/{booking_id}', response_model=BookingModel)
async def get_booking(booking_id: str):
    booking_schema = BookingSchema.objects(id=booking_id).first()
    if booking_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No booking with this id')
    return booking_schema.to_mongo()


@router.delete('/{booking_id}', status_code=204)
async def delete_booking(
    booking_id: str,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    booking_schema = BookingSchema.objects(id=booking_id).first()
    if booking_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No booking with this id')
    if booking_schema.user_id != user_schema.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not owner of booking')
    booking_schema.delete()
