import os

from fastapi import FastAPI

app = FastAPI()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def connect_to_mongo():
    uri = os.getenv("MONGODB_URI")

    global client
    global x1

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    x1 = "It didn't work :("
    try:
        client.admin.command('ping')
        x1 = "It worked :)"
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


connect_to_mongo()


@app.get("/")
async def root():
    return {"message": x1}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
