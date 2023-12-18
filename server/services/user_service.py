import fastapi as _fastapi
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import jwt as _jwt
import fastapi.security as _security
import os

import database as _database
import models.user_model as _models
import schemas as _schemas
from dotenv import load_dotenv

oauth2schema = _security.OAuth2PasswordBearer(tokenUrl='/api/token')


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.email == email).first()


async def create_user(user: _schemas.UserCreate, db: _orm.Session):
    user_obj = _models.User(
        email=user.email, hashed_password=_hash.bcrypt.hash(user.hashed_password)
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


async def auth_user(email: str, password: str, db: _orm.Session):
    user = await get_user_by_email(db=db, email=email)

    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user


async def get_current_user(db: _orm.Session = _fastapi.Depends(get_db), token: str = _fastapi.Depends(oauth2schema)):
    try:
        load_dotenv()
        jwt_secret = os.getenv('JWT_SECRET_KEY', 'anime')
        payload = _jwt.decode(token, jwt_secret, algorithms=['HS256'])
        user = db.query(_models.User).get(payload['id'])
    except Exception:
        raise _fastapi.HTTPException(
            status_code=401, detail='Invalid Email or Password'
        )

    return _schemas.User.from_orm(user)
