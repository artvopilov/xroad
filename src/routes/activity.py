from datetime import date
from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from src.models import (
    Activity as ActivityModel,
    ActivityCreate as ActivityCreateModel,
    ActivityUpdate as ActivityUpdateModel,
    Slot as SlotModel, SlotCreate as SlotCreateModel)
from src.route_deps import RouteDeps
from src.schemas import Activity as ActivitySchema, Slot as SlotSchema, User as UserSchema

router = APIRouter(prefix='/activity', tags=['activity'])


@router.post('', response_model=ActivityModel)
async def create_activity(
    activity_create_model: ActivityCreateModel,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    activity_create_info = activity_create_model.dict()
    activity_schema = ActivitySchema(**activity_create_info, user_id=user_schema.id).save()
    return activity_schema.to_mongo()


@router.get('', response_model=list[ActivityModel])
async def get_activities(skip: int = None, limit: int = None):
    activity_schemas = ActivitySchema.objects[skip: limit]
    return list(activity_schemas.as_pymongo())


@router.get('/{activity_id}', response_model=ActivityModel)
async def get_activity(activity_id: str):
    activity_schema = ActivitySchema.objects(id=activity_id).first()
    if activity_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No activity with this id')
    return activity_schema.to_mongo()


@router.delete('/{activity_id}', status_code=204)
async def delete_activity(
    activity_id: str,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    activity_schema = ActivitySchema.objects(id=activity_id).first()
    if activity_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No activity with this id')
    if activity_schema.user_id != user_schema.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not owner of activity')
    activity_schema.delete()


@router.patch('/{activity_id}', response_model=ActivityModel)
async def update_activity(
    activity_id: str,
    activity_update_model: ActivityUpdateModel,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    activity_schema = ActivitySchema.objects(id=activity_id).first()
    if activity_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No activity with this id')
    if activity_schema.user_id != user_schema.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not owner of activity')
    activity_update_info = activity_update_model.dict(exclude_unset=True)
    activity_schema.update(**activity_update_info)
    return activity_schema.to_mongo()


@router.post('/{activity_id}/slot', response_model=SlotModel)
async def create_slot(
    activity_id: str,
    slot_create_model: SlotCreateModel,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    activity_schema = ActivitySchema.objects(id=activity_id).first()
    if activity_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No activity with this id')
    if activity_schema.user_id != user_schema.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not owner of activity')
    slot_create_info = slot_create_model.dict()
    slot_schema = SlotSchema(**slot_create_info, activity_id=activity_schema.id).save()
    return slot_schema.to_mongo()


@router.get('/{activity_id}/slot', response_model=list[SlotModel])
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
