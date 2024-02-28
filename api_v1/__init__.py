from .products.views import router as products_router

from api_v1.users.manager import get_user_manager

from api_v1.users.schemas import UserCreate
from api_v1.users.schemas import UserRead

from api_v1.users.auth import auth_backend

from api_v1.users.views import router as users_router
from api_v1.profiles.views import router as profiles_router
from fastapi_users import FastAPIUsers

from fastapi import APIRouter

from core.models import User


router = APIRouter()


router.include_router(router=products_router, prefix='/products')
router.include_router(router=users_router, prefix='/users')
router.include_router(router=profiles_router, prefix='/profiles')


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)


router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)