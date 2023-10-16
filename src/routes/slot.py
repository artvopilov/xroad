from datetime import date
from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from src.models import Slot as SlotModel, SlotCreate as SlotCreateModel, SlotUpdate as SlotUpdateModel
from src.route_deps import RouteDeps
from src.schemas import User as UserSchema, Activity as ActivitySchema, Slot as SlotSchema

router = APIRouter(prefix='/slots', tags=['slots'])


@router.post('', response_model=SlotModel)
async def create_slot(
    slot_create_model: SlotCreateModel,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    slot_create_info = slot_create_model.dict()
    activity_id = slot_create_info.pop('activity_id')
    activity_schema = ActivitySchema.objects(id=activity_id).first()
    if activity_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No activity with this id')
    if activity_schema.user_id != user_schema.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not owner of activity')
    slot_schema = SlotSchema(**slot_create_info, activity_id=activity_schema.id).save()
    return slot_schema.to_mongo()


@router.get('', response_model=list[SlotModel])
async def get_slots(
    activity_id: str,
    date_min: date,
    date_max: date,
    skip: int = None,
    limit: int = None
):
    slot_schemas = SlotSchema.objects(
        activity_id=activity_id,
        start_date_time__gte=date_min,
        start_date_time__lte=date_max
    )[skip: limit]
    return list(slot_schemas.as_pymongo())


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


@router.patch('/{slot_id}', response_model=SlotModel)
async def update_slot(
    slot_id: str,
    slot_update_model: SlotUpdateModel,
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
    slot_update_info = slot_update_model.dict(exclude_unset=True)
    slot_schema.update(**slot_update_info)
    return slot_schema.to_mongo()
