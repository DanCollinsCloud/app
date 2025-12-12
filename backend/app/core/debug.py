from fastapi import APIRouter

from app.core.config import config

router = APIRouter(prefix="/config", tags=["Config"])


@router.get("")
async def get_config():
    return {
        "app_name": config.app_name,
        "debug": config.debug,
        "db_url": config.db_url,
    }
