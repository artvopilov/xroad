from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.auth_utils import AuthUtils
from src.models import BusinessCreate as BusinessCreateModel, Business as BusinessModel
from src.route_deps import RouteDeps
from src.schemas import Business as BusinessSchema

router = APIRouter(prefix='/business')


@router.post('/signup', response_model=BusinessModel)
async def signup(business_create_model: BusinessCreateModel):
    business_schema = BusinessSchema.objects(username=str(business_create_model.username)).first()
    if business_schema:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Business with this username already exists')
    business_create_info = business_create_model.dict()
    business_create_info['password'] = AuthUtils.compute_password_hash(business_create_info['password'])
    business_schema = BusinessSchema(**business_create_info).save()
    return business_schema.to_mongo()


@router.post('/signin')
async def signin(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    business_schema = BusinessSchema.objects(username=form_data.username).first()
    if not business_schema or not AuthUtils.verify_password(form_data.password, business_schema.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Incorrect username or password')
    access_token = AuthUtils.create_access_token(business_schema.username)
    return {'access_token': access_token, 'token_type': "bearer"}


@router.get('', response_model=BusinessModel)
async def me(business_schema: Annotated[BusinessSchema, Depends(RouteDeps.get_current_business)]):
    return business_schema.to_mongo()
