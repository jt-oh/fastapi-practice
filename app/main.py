from fastapi import FastAPI

from .api.v1 import api
from .database import engine

myApp = FastAPI()

myApp.include_router(api.api_router)


@myApp.get("/")
async def get_root():
    return {"message": "Hello World"}