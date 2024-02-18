from typing import Annotated, Union

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from mongoengine.queryset.visitor import Q

from src.auth_utils import AuthUtils
from src.models import (
    User as UserModel,
    UserSignup as UserSignupModel,
    PersonUpdate as PersonUpdateModel,
    BusinessUpdate as BusinessUpdateModel
)
from src.route_deps import RouteDeps
from src.schemas import User as UserSchema
from src.validator import validate_phone_number, validate_email

router = APIRouter(prefix='/users', tags=['users'])


@router.post(
    '/signup',
    response_model=UserModel,
    response_model_exclude={'password'},
    response_model_exclude_unset=True
)
async def signup(user_signup_model: UserSignupModel):
    if not validate_phone_number(user_signup_model.phone):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not valid phone')
    if user_signup_model.email is not None and not validate_email(user_signup_model.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not valid email')

    if UserSchema.objects(username=str(user_signup_model.username)).first() is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with this username already exists')
    if UserSchema.objects(phone=str(user_signup_model.phone)).first() is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with this phone already exists')
    if (user_signup_model.email is not None
            and UserSchema.objects(email=str(user_signup_model.email)).first() is not None):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with this email already exists')

    user_signup_info = user_signup_model.dict(exclude_unset=True)
    user_signup_info['password'] = AuthUtils.compute_password_hash(user_signup_info['password'])
    user_schema = UserSchema(**user_signup_info).save()
    return user_schema.to_mongo()


@router.post('/signin')
async def signin(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_schema = UserSchema.objects(
        Q(username=form_data.username)
        | Q(phone=form_data.username)
        | Q(email=form_data.username)
    ).first()
    if user_schema is None or not AuthUtils.verify_password(form_data.password, user_schema.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Incorrect username or password')
    access_token = AuthUtils.create_access_token(user_schema.username)
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get(
    '/',
    response_model=UserModel,
    response_model_exclude={'password'},
    response_model_exclude_unset=True
)
async def get(user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]):
    return user_schema.to_mongo()


@router.patch(
    '/',
    response_model=UserModel,
    response_model_exclude={'password'},
    response_model_exclude_unset=True
)
async def update(
        user_update_model: Union[PersonUpdateModel, BusinessUpdateModel],
        user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    user_update_info = user_update_model.dict(exclude_unset=True)
    user_schema.modify(**user_update_info)
    return user_schema.to_mongo()


@router.post(
    '/pro',
    response_model=UserModel,
    response_model_exclude={'password'},
    response_model_exclude_unset=True
)
async def pro(user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]):
    if user_schema.user_type == 'business':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not allowed for business users')
    user_schema.person_is_pro = True
    user_schema.save()
    return user_schema.to_mongo()


@router.post(
    '/verify',
    response_model=UserModel,
    response_model_exclude={'password'},
    response_model_exclude_unset=True
)
async def verify(user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]):
    if user_schema.user_type == 'person':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Not allowed for person users')
    user_schema.business_is_verified = True
    user_schema.save()
    return user_schema.to_mongo()
