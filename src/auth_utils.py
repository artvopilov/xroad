from datetime import timedelta, datetime

from jose import jwt
from passlib.context import CryptContext


class AuthUtils:
    _CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
    _JWT_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    _JWT_ALGORITHM = "HS256"
    _JWT_MINUTES = 60 * 24 * 7

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str):
        return cls._CONTEXT.verify(plain_password, hashed_password)

    @classmethod
    def compute_password_hash(cls, password):
        return cls._CONTEXT.hash(password)

    @classmethod
    def create_access_token(cls, username: str):
        expire = datetime.utcnow() + timedelta(minutes=cls._JWT_MINUTES)
        payload = {'username': username, 'expire': expire}
        return jwt.encode(payload, cls._JWT_SECRET_KEY, algorithm=cls._JWT_ALGORITHM)

    @classmethod
    def extract_access_token_payload(cls, access_token):
        return jwt.decode(access_token, cls._JWT_SECRET_KEY, algorithms=[cls._JWT_ALGORITHM])
