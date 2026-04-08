from typing import List

from fastapi import APIRouter, HTTPException

from . import service
from .schema.schemas import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserRead])
async def list_users():
    return service.list_users()


@router.post("/", response_model=UserRead)
async def create_user(payload: UserCreate):
    return service.create_user(payload)


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int):
    u = service.get_user(user_id)
    if not u:
        raise HTTPException(status_code=404, detail="User not found")
    return u


@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, payload: UserUpdate):
    u = service.update_user(user_id, payload)
    if not u:
        raise HTTPException(status_code=404, detail="User not found")
    return u


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    ok = service.delete_user(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status": "deleted"}
