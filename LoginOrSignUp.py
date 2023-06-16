from http.client import HTTPException

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users import BaseUserManager, exceptions
from fastapi_users.authentication import Strategy
from fastapi_users.router import ErrorCode
from flask import Request
from starlette import status

import auth.auth
from auth.manager import get_user_manager
from auth.schemas import UserRead
from models import models

routerLogin = APIRouter()


@routerLogin.get("/authorize")
async def login_or_sign_up(
        request: Request,
        user_create: user_create_schema,  # type: ignore
        credentials: OAuth2PasswordRequestForm = Depends(),
        strategy: Strategy[models.UP, models.ID] = Depends(auth.auth.auth_backend.get_strategy),
        user_manager: BaseUserManager = Depends(get_user_manager)
):

    backend = auth.auth.auth_backend
    user_in_db = await user_manager.get_by_email(credentials.username)
    if user_in_db is None or not user_in_db.is_active:
        #do register
        try:
            created_user = await user_manager.create(
                user_create, safe=True, request=request
            )
        except exceptions.UserAlreadyExists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.REGISTER_USER_ALREADY_EXISTS,
            )
        except exceptions.InvalidPasswordException as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "code": ErrorCode.REGISTER_INVALID_PASSWORD,
                    "reason": e.reason,
                },
            )

        return UserRead.from_orm(created_user)
    else:
        # do login
        user = await user_manager.authenticate(credentials)
        response = await backend.login(strategy, user)
        await user_manager.on_after_login(user, request, response)
        return response


