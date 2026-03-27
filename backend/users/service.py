from typing import List

from . import repository
from .schema.schemas import UserCreate, UserRead, UserUpdate


def list_users() -> List[UserRead]:
    users = repository.list_users()
    return [UserRead(id=u.id, email=u.email, name=u.name) for u in users]


def create_user(data: UserCreate) -> UserRead:
    user = repository.create_user(email=data.email, name=data.name)
    return UserRead(id=user.id, email=user.email, name=user.name)


def get_user(user_id: int) -> UserRead | None:
    u = repository.get_user(user_id)
    if not u:
        return None
    return UserRead(id=u.id, email=u.email, name=u.name)


def update_user(user_id: int, data: UserUpdate) -> UserRead | None:
    u = repository.update_user(user_id, name=data.name)
    if not u:
        return None
    return UserRead(id=u.id, email=u.email, name=u.name)


def delete_user(user_id: int) -> bool:
    return repository.delete_user(user_id)
