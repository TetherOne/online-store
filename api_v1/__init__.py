from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from core.models import User
from api_v1.users.views import user_router
from api_v1.users.auth import auth_backend
from api_v1.users.manager import get_user_manager
from api_v1.users.schemas import UserRead, UserCreate
from .products.views import router as products_router

router = APIRouter()

router.include_router(router=products_router, prefix='/products')
router.include_router(router=user_router, prefix='/users')


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/users",
    tags=["Users"],
)


router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/users",
    tags=["Users"],
)