from fastapi import FastAPI

from .api.v1 import api
from .database import engine

myApp = FastAPI()

# simple database migrations if there isn't migration tools
# models.Base.metadata.create_all(bind=engine)

myApp.include_router(api.api_router)

@myApp.get("/")
async def get_root():
    return {"message": "Hello World"}