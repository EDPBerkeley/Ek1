import os

from fastapi import FastAPI

import uvicorn

from routes import product_routes, product_data_routes, store_overview_data_routes

app = FastAPI()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from app.routes import shop_routes

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


app.include_router(shop_routes.router, prefix="/store", tags=["store"])
app.include_router(product_routes.router, prefix="/product", tags=["product"])
app.include_router(product_data_routes.router, prefix="/product_data", tags=["product_data"])
app.include_router(store_overview_data_routes.router, prefix="/store_overview_data", tags=["store_overview_data"])


DBUtils.initiate_connection()
# if __name__ == 'main':
#     uvicorn.run("app:main", host="0.0.0.0", port=8000)
# store_routes.get_stores_within_boundary(( -122.27300, 37.87150), (-122.24174, 37.90564))