from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from src.models import (
    Activity as ActivityModel,
    ActivityCreate as ActivityCreateModel,
    ActivityUpdate as ActivityUpdateModel
)
from src.route_deps import RouteDeps
from src.schemas import Activity as ActivitySchema, User as UserSchema

router = APIRouter(prefix='/activities', tags=['activities'])


@router.post('', response_model=ActivityModel)
async def create_activity(
    activity_create_model: ActivityCreateModel,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    if user_schema.user_type != 'business' and not user_schema.is_pro:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not allowed')
    activity_create_info = activity_create_model.dict()
    activity_schema = ActivitySchema(**activity_create_info, user_id=user_schema.id).save()
    return activity_schema.to_mongo()


@router.get('', response_model=list[ActivityModel])
async def get_activities(
    min_x: int,
    min_y: int,
    max_x: int,
    max_y: int,
    user_id: str = None,
    skip: int = 0,
    limit: int = 10
):
    activity_schemas = ActivitySchema.objects(x__gte=min_x, y__gte=min_y, x__lte=max_x, y__lte=max_y)
    if user_id is not None:
        activity_schemas = activity_schemas(user_id=user_id)
    activity_schemas = activity_schemas[skip: limit]
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
    activity_schema.modify(**activity_update_info)
    return activity_schema.to_mongo()
