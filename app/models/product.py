from dataclasses import Field

from mongoengine import *
from pydantic import BaseModel, Field
from datetime import datetime
from bson.objectid import ObjectId

from models.mongo_model import MongoModel, OID


class Product(Document):
    name = StringField()
    description = StringField()
    price = DecimalField()
    category = IntField()
    sku = StringField()
    quantity = IntField()
    date_created = DateTimeField()




# class ProductJSONModel(MongoModel):
#     id: OID=Field()
#     name: str=Field()
#     description: str=Field()
#     price: float=Field()
#     category: int=Field()
#     sku: str=Field()
#     quantity: int=Field()
#     date_created: datetime=Field()
