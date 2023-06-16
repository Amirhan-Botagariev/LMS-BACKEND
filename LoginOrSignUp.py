from fastapi import APIRouter, Depends
from fastapi_users import BaseUserManager

from CreateUser import create_user
from auth.manager import get_user_manager
from models import models

routerLogin = APIRouter()


@routerLogin.post("/authorize")
async def login_or_sign_up(email: str,
                           password: str,
                           user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager)):
    await create_user(email, password, "123", False, user_manager)
