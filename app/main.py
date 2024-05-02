import os

from fastapi import FastAPI

from routes import shop_routes, product_routes, store_overview_data_routes, user_routes
from utils.db_utils import DBUtils

app = FastAPI()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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


app.include_router(shop_routes.router, prefix="/store", tags=["store"])
app.include_router(product_routes.router, prefix="/product", tags=["product"])
app.include_router(store_overview_data_routes.router, prefix="/store_overview_data", tags=["store_overview_data"])
app.include_router(user_routes.router, prefix="/user", tags=["user"])

DBUtils.initiate_connection()
