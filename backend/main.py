from fastapi import FastAPI

from backend.core.config import get_settings
from backend.core.database import init_db
from backend.tickets.router import router as tickets_router
from backend.users.router import router as users_router


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(title=settings.APP_NAME)

    # initialize DB (placeholder)
    init_db(settings.DATABASE_URL)

    # include feature routers
    app.include_router(users_router)
    app.include_router(tickets_router)

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
