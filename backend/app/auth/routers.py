from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from app.auth.models import User
from app.auth.utils import get_user_manager
from app.database import UserDB, Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI Users instance
fastapi_users = FastAPIUsers(get_user_manager, [JWT_SECRET])

router = APIRouter()

router.include_router(fastapi_users.get_auth_router(), prefix="/auth", tags=["auth"])
router.include_router(fastapi_users.get_register_router(), prefix="/auth", tags=["auth"])
