from fastapi import FastAPI

myApp = FastAPI()


@myApp.get("/")
async def root():
    return {"message": "Hello World"}