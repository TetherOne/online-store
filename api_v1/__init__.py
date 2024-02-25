from fastapi import APIRouter
from api_v1.users.views import user_router
from .products.views import router as products_router

router = APIRouter()

router.include_router(router=products_router, prefix='/products')
router.include_router(router=user_router, prefix='/users')
