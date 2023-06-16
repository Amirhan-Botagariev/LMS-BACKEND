import contextlib
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users import BaseUserManager
from fastapi_users.exceptions import UserAlreadyExists

from auth.database import get_async_session, get_user_db
from auth.manager import get_user_manager
from auth.schemas import UserCreate
from models import models

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def create_user(email: str, password: str, avatar: str, is_superuser: bool = False,
                      user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager), ):
    try:
        user = await user_manager.create(
            UserCreate(
                email=email, password=password, is_superuser=is_superuser, avatar=avatar
            )
        )
        await user_manager.authenticate(
            credentials=OAuth2PasswordRequestForm(username=email, password=password, scope=""))
        await read_items()


    except UserAlreadyExists:
        print(f"User {email} already exists")
        await user_manager.authenticate(
            credentials=OAuth2PasswordRequestForm(username=email, password=password, scope=""))


async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}