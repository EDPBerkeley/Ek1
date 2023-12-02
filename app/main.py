import os

from fastapi import FastAPI

app = FastAPI()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from app.routes import store_routes

from app.utils.db_utils import DBUtils

global client
global x1

try:
    client = MongoClient(os.getenv("MONGODB_URI"), server_api=ServerApi('1'))
except:
    print("Couldn't connect to DB")


@app.get("/")
async def root():
    return "Hello World"


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(store_routes.router, prefix="/store", tags=["store"])


DBUtils.initiate_connection()
# store_routes.get_stores_within_boundary(( -122.27300, 37.87150), (-122.24174, 37.90564))