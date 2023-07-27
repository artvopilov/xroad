from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from src.models import Service as ServiceModel, ServiceCreate as ServiceCreateModel
from src.route_deps import RouteDeps
from src.schemas import Business as BusinessSchema, Service as ServiceSchema

router = APIRouter(prefix='/service')


@router.post('/create', response_model=ServiceModel)
async def create(
    service_create_model: ServiceCreateModel,
    business_schema: Annotated[BusinessSchema, Depends(RouteDeps.get_current_business)]
):
    service_create_info = service_create_model.dict()
    service_schema = ServiceSchema(**service_create_info, business_id=business_schema.id).save()
    service_info = service_schema.to_mongo()
    return service_info


@router.get('/get/{id_}', response_model=ServiceModel)
async def get(id_: str):
    service_schema = ServiceSchema.objects(id=id_).first()
    if not service_schema:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Service with this id does not exist')
    service_info = service_schema.to_mongo()
    return service_info
