from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from src.models import Slot as SlotModel, Booking as BookingModel
from src.route_deps import RouteDeps
from src.schemas import (
    User as UserSchema,
    Booking as BookingSchema,
    Activity as ActivitySchema,
    Slot as SlotSchema)

router = APIRouter(prefix='/slot', tags=['slot'])


@router.get('/{slot_id}', response_model=SlotModel)
async def get_slot(slot_id: str):
    slot_schema = SlotSchema.objects(id=slot_id).first()
    if slot_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No slot with this id')
    return slot_schema.to_mongo()


@router.delete('/{slot_id}', status_code=204)
async def delete_slot(
    slot_id: str,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    slot_schema = SlotSchema.objects(id=slot_id).first()
    if slot_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No slot with this id')
    activity_schema = ActivitySchema.objects(id=slot_schema.activity_id).first()
    if activity_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No activity with this id')
    if activity_schema.user_id != user_schema.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not owner of activity')
    slot_schema.delete()


@router.post('/{slot_id}/booking', response_model=BookingModel)
async def create_booking(
    slot_id: str,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    slot_schema = SlotSchema.objects(id=slot_id).first()
    if slot_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No slot with this id')
    slot_schema = BookingSchema(slot_id=slot_schema.id, user_id=user_schema.id).save()
    return slot_schema.to_mongo()


@router.get('/{slot_id}/booking', response_model=list[BookingModel])
async def get_bookings(slot_id: str, skip: int = None, limit: int = None):
    booking_schemas = BookingSchema.objects(slot_id=slot_id)[skip: limit]
    return list(booking_schemas.as_pymongo())
