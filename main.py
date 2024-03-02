from api_v1 import router as router_v1
from redis import asyncio as aioredis
from core.config import settings
from fastapi_cache import FastAPICache
from fastapi import FastAPI
from fastapi_cache.backends.redis import RedisBackend
import uvicorn



app = FastAPI()


app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
redis = aioredis.from_url("redis://127.0.0.1:6379", encoding="utf-8", decode_responses=True)
FastAPICache.init(RedisBackend(redis), prefix="store-cache")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
