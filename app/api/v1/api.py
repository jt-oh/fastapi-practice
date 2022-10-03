from fastapi import APIRouter

from api.v1.endpoints import items, users

api_router = APIRouter()

api_router.include_router(users.router, tags=["users"])
api_router.include_router(items.router, tags=["items"])