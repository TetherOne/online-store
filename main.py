from api_v1 import router as router_v1, fastapi_users
from core.config import settings

from fastapi import Request, Depends
from fastapi import FastAPI

import uvicorn

from core.models import User

app = FastAPI()
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def hello_world(request: Request):
    return {"message": "hello world"}


current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
