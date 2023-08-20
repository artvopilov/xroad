from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from src.models import Booking as BookingModel
from src.route_deps import RouteDeps
from src.schemas import User as UserSchema, Booking as BookingSchema

router = APIRouter(prefix='/booking', tags=['booking'])


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
