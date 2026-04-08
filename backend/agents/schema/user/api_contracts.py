from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr
from users.enums.enums import RoleEnum, UserStatusEnum


class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    role: set[RoleEnum]
    title: Optional[str] = "Customer"


class UserUpdateRequest(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[set[RoleEnum]]
    title: Optional[str]
    isActive: Optional[UserStatusEnum]


class UserDeleteRequest(BaseModel):
    email: EmailStr


class UserReadResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: set[RoleEnum]
    title: Optional[str]
    LastLogin: datetime
    isActive: UserStatusEnum
    createdAt: datetime
    updatedAt: datetime


class UserListResponse(BaseModel):
    total: int
    users: List[UserReadResponse]
