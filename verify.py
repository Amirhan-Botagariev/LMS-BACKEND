from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi_users import BaseUserManager, exceptions
from fastapi_users.router import ErrorCode
from starlette import status

from auth.manager import get_user_manager
from auth.schemas import UserRead

router = APIRouter()


@router.get("/verify")
async def test(request: Request,
               token,
               user_manager: BaseUserManager = Depends(get_user_manager)):
    try:
        user = await user_manager.verify(token, request)
        return UserRead.from_orm(user)
    except (exceptions.InvalidVerifyToken, exceptions.UserNotExists):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorCode.VERIFY_USER_BAD_TOKEN,
        )
    except exceptions.UserAlreadyVerified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ErrorCode.VERIFY_USER_ALREADY_VERIFIED,
        )
