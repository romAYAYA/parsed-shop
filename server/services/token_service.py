from dotenv import load_dotenv
import os
import jwt as _jwt
from fastapi import HTTPException
import datetime

import schemas as _schemas
import models.user_model as _models

load_dotenv()
jwt_secret = os.getenv('JWT_SECRET_KEY', 'anime')

if jwt_secret is None:
    raise HTTPException(status_code=500, detail="JWT secret key not configured")


async def create_token(user: _models.User):
    user_obj = _schemas.User.from_orm(user)
    token = _jwt.encode(user_obj.dict(), jwt_secret)
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    payload = {
        'sub': user.id,
        'exp': expiration_time.timestamp(),
    }

    return dict(payload, access_token=token, token_type='bearer')
