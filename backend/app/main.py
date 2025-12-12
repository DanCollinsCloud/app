from fastapi import FastAPI

from app.api.v1 import user
from app.core.config import config
from app.core.logging import setup_logging
from app.db.schema import Base, engine

setup_logging()
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=config.app_name,
    version="1.0.0",
    description="API for user management",
    docs_url="/api/docs" if config.debug else None,
    redoc_url="/api/redoc" if config.debug else None,
)


# Register routes
app.include_router(user.router, prefix="/api/v1")

# Conditionally include debug endpoints
if config.debug:
    from app.core import debug, health

    app.include_router(health.router)
    app.include_router(debug.router)
