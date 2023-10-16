from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.auth_utils import AuthUtils
from src.models import User as UserModel, UserSignup as UserSignupModel, UserUpdate as UserUpdateModel
from src.route_deps import RouteDeps
from src.schemas import User as UserSchema

router = APIRouter(prefix='/users', tags=['users'])


@router.post(
    '/signup',
    response_model=UserModel,
    response_model_exclude={'password'},
    response_model_exclude_unset=True
)
async def signup(user_signup_model: UserSignupModel):
    user_schema = UserSchema.objects(username=str(user_signup_model.username))
    if user_schema:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with this username already exists')
    user_signup_info = user_signup_model.dict(exclude_unset=True)
    user_signup_info['password'] = AuthUtils.compute_password_hash(user_signup_info['password'])
    user_schema = UserSchema(**user_signup_info).save()
    return user_schema.to_mongo()


@router.post('/signin')
async def signin(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_schema = UserSchema.objects(username=form_data.username).first()
    if not user_schema or not AuthUtils.verify_password(form_data.password, user_schema.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Incorrect username or password')
    access_token = AuthUtils.create_access_token(user_schema.username)
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/', response_model=UserModel, response_model_exclude={'password'}, response_model_exclude_unset=True)
async def get(user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]):
    return user_schema.to_mongo()


@router.patch('/', response_model=UserModel, response_model_exclude={'password'}, response_model_exclude_unset=True)
async def update(
    user_update_model: UserUpdateModel,
    user_schema: Annotated[UserSchema, Depends(RouteDeps.get_current_user)]
):
    user_update_info = user_update_model.dict(exclude_unset=True)
    user_schema.modify(**user_update_info)
    return user_schema.to_mongo()
