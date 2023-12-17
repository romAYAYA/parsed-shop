import fastapi as _fastapi
from fastapi import APIRouter
import sqlalchemy.orm as _orm
import services.user_service as _services
import schemas as _schemas

router = APIRouter()


@router.post("/api/users")
async def create_user(user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    try:
        user = await _services.create_user(user, db)
        return user
    except Exception as e:
        return e


@router.get("/hi")
def hi_user():
    return {"message": "Hi asdfsgfsdgfsdh"}
