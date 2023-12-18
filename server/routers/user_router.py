import fastapi as _fastapi
from fastapi import APIRouter
import fastapi.security as _security

import sqlalchemy.orm as _orm

import services.user_service as _user_service
import services.token_service as _token_service

import schemas as _schemas

router = APIRouter()


@router.post("/api/register")
async def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_user_service.get_db)
):
    try:
        db_user = await _user_service.get_user_by_email(user.email, db)

        if db_user:
            raise _fastapi.HTTPException(status_code=400, detail="Email already in use")

        user = await _user_service.create_user(user, db)
        return await _token_service.create_token(user)
    except Exception as err:
        return err


@router.get("/api/users/my_profile", response_model=_schemas.User)
async def get_user(
    user: _schemas.User = _fastapi.Depends(_user_service.get_current_user),
):
    return user


@router.post("/api/login")
async def login(
    form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(),
    db: _orm.Session = _fastapi.Depends(_user_service.get_db),
):
    user = await _user_service.auth_user(form_data.username, form_data.password, db)
    if not user:
        raise _fastapi.HTTPException(status_code=401, detail="Invalid credentials")

    return await _token_service.create_token(user)
