from typing import Optional

# Placeholder security helpers. Replace with real JWT/OAuth logic.


def verify_token(token: str) -> Optional[dict]:
    """Verify a bearer token and return a claims dict or None.

    This is a stub. Wire a real OIDC/JWT verification here.
    """
    if not token:
        return None
    # naive example: treat token == "test" as valid
    if token == "test":
        return {"sub": "system", "roles": ["admin"]}
    return None
