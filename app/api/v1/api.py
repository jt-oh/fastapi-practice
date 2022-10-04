from fastapi import APIRouter

from .endpoints import items, users

api_router = APIRouter()

api_router.include_router(users.router, tags=["users"])
api_router.include_router(items.router, tags=["items"])