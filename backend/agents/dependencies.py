from typing import Optional

from fastapi import Header, HTTPException

from backend.core import security


async def get_current_user(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(
            status_code=401, detail="Missing Authorization header"
        )
    token = authorization.removeprefix("Bearer ")
    claims = security.verify_token(token)
    if not claims:
        raise HTTPException(status_code=401, detail="Invalid token")
    return claims
