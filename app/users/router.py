from fastapi import APIRouter, Depends, Response, status

from app.exceptions import (
    IncorrectEmailOrPasswordException,
    UserAlreadyExistsException
)
from app.users.auth import (
    authenticate_user,
    create_access_token,
    get_password_hash
)
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SAccessToken, SUser, SUserAuth


router_auth = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

router_users = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router_auth.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: SUserAuth
) -> None:
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(password=user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router_auth.post("/login", status_code=status.HTTP_200_OK)
async def login_user(
    response: Response,
    user_data: SUserAuth
) -> SAccessToken:
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token(data={"sub": str(user.id)})
    response.set_cookie(
        key="booking_access_token",
        value=access_token,
        httponly=True
    )
    return SAccessToken(access_token=access_token).model_dump()


@router_auth.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout_user(
    response: Response
) -> None:
    response.delete_cookie(key="booking_access_token")


@router_users.get("/me", status_code=status.HTTP_200_OK)
async def read_users_me(
    current_user: Users = Depends(get_current_user)
) -> SUser:
    return current_user
