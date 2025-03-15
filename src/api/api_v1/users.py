from typing import Annotated
from fastapi import APIRouter, Depends
from core.config import settings
from crud.users import get_all_users, create_user as create_user_crud
from core.schemas.user import UserRead, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper

router = APIRouter(tags=["users"])


@router.get("/", response_model=list[UserRead])
async def get_users(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    users = await get_all_users(session=session)
    return users


@router.post("/", response_model=UserRead)
async def create_user(
    user_create: UserCreate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> UserRead:
    user = await create_user_crud(
        session=session, 
        user_create=user_create)
    return user

