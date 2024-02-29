from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from api_v1 import router as router_v1
from config import REDIS_PORT, REDIS_HOST

from core.config import settings

from fastapi import Request
from fastapi import FastAPI

import uvicorn



app = FastAPI()


app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf-8", decode_responses=True)
FastAPICache.init(RedisBackend(redis), prefix="Online-Store-cache")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
