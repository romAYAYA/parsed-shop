from dotenv import load_dotenv
import os
import jwt as _jwt
from fastapi import HTTPException
import fastapi.security as _security

import schemas as _schemas
import models.user_model as _models

load_dotenv()
jwt_secret = os.getenv('JWT_SECRET_KEY', 'anime')

oauth2schema = _security.OAuth2PasswordBearer(tokenUrl='/api/token')

if jwt_secret is None:
    raise HTTPException(status_code=500, detail="JWT secret key not configured")


async def create_token(user: _models.User):
    user_obj = _schemas.User.from_orm(user)
    token = _jwt.encode(user_obj.dict(), jwt_secret)
    return dict(access_token=token, token_type='bearer')
