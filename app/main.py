from fastapi import FastAPI

from .api.v1 import api
from .database import engine

myApp = FastAPI()

# models.Base.metadata.create_all(bind=engine)

myApp.include_router(api.api_router)