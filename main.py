from fastapi.testclient import TestClient

from api_v1 import router as router_v1

from core.config import settings

from fastapi import Request
from fastapi import FastAPI

import uvicorn



app = FastAPI()
client = TestClient(app)

app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
