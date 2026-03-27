from typing import List, Optional

from pydantic import BaseModel
from users.enums.enums import RoleEnum


class RoleCreateRequest(BaseModel):
    name: RoleEnum
    description: str


class RoleUpdateRequest(BaseModel):
    name: RoleEnum
    description: Optional[str]


class RoleDeleteRequest(BaseModel):
    name: RoleEnum


class RoleReadResponse(BaseModel):
    name: RoleEnum
    description: str


class RoleListResponse(BaseModel):
    total: int
    roles: List[RoleReadResponse]
