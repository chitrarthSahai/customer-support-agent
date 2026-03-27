from typing import List, Optional

from .model.models import User

# In-memory repository for early development. Swap with DB-backed repository.

_users: List[User] = []


def list_users() -> List[User]:
    return _users.copy()


def get_user(user_id: int) -> Optional[User]:
    for u in _users:
        if u.id == user_id:
            return u
    return None


def create_user(email: str, name: str) -> User:
    user = User(email=email, name=name)
    _users.append(user)
    return user


def update_user(user_id: int, name: str) -> Optional[User]:
    user = get_user(user_id)
    if not user:
        return None
    user.name = name
    return user


def delete_user(user_id: int) -> bool:
    global _users
    user = get_user(user_id)
    if not user:
        return False
    _users = [u for u in _users if u.id != user_id]
    return True
