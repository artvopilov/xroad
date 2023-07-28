from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from datetime import date

from src.models import (
    Service as ServiceModel,
    ServiceCreate as ServiceCreateModel,
    ServiceSlot as ServiceSlotModel, ServiceSlotCreate as ServiceSlotCreateModel,
    ServiceSlotBooking as ServiceSlotBookingModel)
from src.route_deps import RouteDeps
from src.schemas import (
    User as UserSchema,
    Business as BusinessSchema,
    Service as ServiceSchema,
    ServiceSlot as ServiceSlotSchema,
    ServiceSlotBooking as ServiceSlotBookingSchema)

router = APIRouter(prefix='/service')


@router.post('', response_model=ServiceModel)
async def create_service(
    service_create_model: ServiceCreateModel,
    business_schema: Annotated[BusinessSchema, Depends(RouteDeps.get_current_business)]
):
    service_create_info = service_create_model.dict()
    service_schema = ServiceSchema(**service_create_info, business_id=business_schema.id).save()
    return service_schema.to_mongo()


@router.get('', response_model=list[ServiceModel])
async def get_services(skip: int = None, limit: int = None):
    service_schemas = ServiceSchema.objects[skip: limit]
    return list(service_schemas.as_pymongo())


@router.get('/{service_id}', response_model=ServiceModel)
async def get_service_by_id(service_id: str):
    service_schema = ServiceSchema.objects(id=service_id).first()
    if service_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No service with this id')
    return service_schema.to_mongo()


@router.post('/{service_id}/slot', response_model=ServiceSlotModel)
async def create_service_slot(
    service_id: str,
    service_slot_create_model: ServiceSlotCreateModel,
    business_schema: Annotated[BusinessSchema, Depends(RouteDeps.get_current_business)]
):
    service_schema = ServiceSchema.objects(id=service_id).first()
    if service_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No service with this id')
    if service_schema.business_id != business_schema.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not owner of service')
    service_slot_create_info = service_slot_create_model.dict()
    service_slot_schema = ServiceSlotSchema(**service_slot_create_info, service_id=service_schema.id).save()
    return service_slot_schema.to_mongo()


@router.get('/{service_id}/slot', response_model=list[ServiceSlotModel])
async def get_service_slots(service_id: str, date_min: date, date_max: date = None, skip: int = None, limit: int = None):
    service_slot_schemas = ServiceSlotSchema.objects(
        service_id=service_id, start_date_time__gte=date_min, start_date_time__lte=date_max)[skip: limit]
    return list(service_slot_schemas.as_pymongo())


@router.get('/slot/{slot_id}', response_model=ServiceSlotModel)
async def get_service_slot_by_id(slot_id: str):
    service_slot_schema = ServiceSlotSchema.objects(id=slot_id).first()
    if service_slot_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No service slot with this id')
    return service_slot_schema.to_mongo()


@router.post('/slot/{slot_id}/booking', response_model=ServiceSlotBookingModel)
async def create_service_slot_booking(
    slot_id: str,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    service_slot_schema = ServiceSlotSchema.objects(id=slot_id).first()
    if service_slot_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No service slot with this id')
    service_slot_schema = ServiceSlotBookingSchema(slot_id=service_slot_schema.id, user_id=user_schema.id).save()
    return service_slot_schema.to_mongo()


@router.get('/slot/{slot_id}/booking', response_model=list[ServiceSlotBookingModel])
async def get_service_slot_booking(slot_id: str, skip: int = None, limit: int = None):
    service_slot_booking_schemas = ServiceSlotBookingSchema.objects(slot_id=slot_id)[skip: limit]
    return list(service_slot_booking_schemas.as_pymongo())


@router.get('/slot/booking/{booking_id}', response_model=ServiceSlotBookingModel)
async def get_service_slot_by_id(booking_id: str):
    service_slot_booking_schema = ServiceSlotBookingSchema.objects(id=booking_id).first()
    if service_slot_booking_schema is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No service slot booking with this id')
    return service_slot_booking_schema.to_mongo()
