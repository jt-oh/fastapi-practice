from typing import Union
from fastapi import FastAPI, Query

from pydantic import BaseModel, Field

myApp = FastAPI()

fakeItems = [
    {"name": "tom", "email": "tom@nomail.com", "password": "tomPassword", "age": 25, "birth_place": "london"},
    {"name": "jack", "email": "jack@nomail.com", "password": "jackPassword", "age": 21, "birth_place": "belgium"},
    {"name": "tina", "email": "tina@nomail.com", "password": "tinaPassword", "age": 28, "birth_place": "arizona"},
    {"name": "christin", "email": "christin@nomail.com", "password": "christinPassword", "age": 24, "birth_place": "berlin"},
    {"name": "michael", "email": "miachael@nomail.com", "password": "miachaelPassword", "age": 34, "birth_place": "newyork"},
    {"name": "sonya", "email": "sonya@nomail.com", "password": "sonyaPassword", "age": 19, "birth_place": "bern"},
]

class RequestItem(BaseModel):
    name: str = "world"
    email: str = "world@nomail.com"
    password: str
    age: int = Field(default=20, ge=0)
    birth_place: str = Field(default="seoul", alias="birth-place")

class ResponseItem(BaseModel):
    name: str = "world"
    email: str = "world@nomail.com"
    age: int = Field(default=20, ge=0)
    birth_place: str = Field(default="seoul", alias="birth-place")

@myApp.get("/")
async def root(name: str = "World"):
    return {"message": "Hello " + name}

@myApp.get("/my-items")
async def get_my_items_list(query_param: bool = Query(default=True)):
    return fakeItems

@myApp.get("/my-items/{item_id}")
async def get_my_item(item_id: int, query_param: bool = False):
    return {"item_id": item_id, "query_param": query_param}

@myApp.post("/my-items", response_model=ResponseItem)
async def post_my_item(*, query_param: bool = Query(default=False), is_query: Union[bool, None] = Query(default=None), item: RequestItem):
    return item

@myApp.put("/my-items/{item_id}", response_model=ResponseItem)
async def update_my_item(*, query_param: bool = Query(default=False, example=True), item: RequestItem):
    return item