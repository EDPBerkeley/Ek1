from dataclasses import Field

from mongoengine import *
from pydantic import BaseModel, Field
from datetime import datetime
from bson.objectid import ObjectId

from models.mongo_model import MongoModel, OID
from models.one_image import OneImage


class Product(Document):
    name = StringField()
    description = StringField()
    price = DecimalField()
    category = StringField()
    sku = StringField()
    quantity = IntField()
    date_created = DateTimeField()
    images = EmbeddedDocumentListField(OneImage)




# class ProductJSONModel(MongoModel):
#     id: OID=Field()
#     name: str=Field()
#     description: str=Field()
#     price: float=Field()
#     category: int=Field()
#     sku: str=Field()
#     quantity: int=Field()
#     date_created: datetime=Field()
