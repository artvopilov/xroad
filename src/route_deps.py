from datetime import datetime, timezone
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from src.auth_utils import AuthUtils
from src.schemas import User as UserSchema, Business as BusinessSchema


class RouteDeps:
    OAUTH2_SCHEME_USER = OAuth2PasswordBearer(tokenUrl='user/signin')
    OAUTH2_SCHEME_BUSINESS = OAuth2PasswordBearer(tokenUrl='business/signin')

    @classmethod
    async def get_current_user(cls, access_token: Annotated[str, Depends(OAUTH2_SCHEME_USER)]) -> UserSchema:
        username = cls._get_current_username(access_token)
        user_schema = UserSchema.objects(username=username).first()
        if not user_schema:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username')
        return user_schema

    @classmethod
    async def get_current_business(
        cls,
        access_token: Annotated[str, Depends(OAUTH2_SCHEME_BUSINESS)]
    ) -> BusinessSchema:
        username = cls._get_current_username(access_token)
        business_schema = BusinessSchema.objects(username=username).first()
        if not business_schema:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username')
        return business_schema

    @classmethod
    def _get_current_username(cls, access_token: str):
        try:
            payload = AuthUtils.extract_access_token_payload(access_token)
            username = payload.get('username')
            expire = payload.get('expire')
            if username is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Missing username')
            if datetime.fromtimestamp(expire, tz=timezone.utc) < datetime.now(tz=timezone.utc):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token expired')
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')
        return username
