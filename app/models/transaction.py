from mongoengine import *

from app.models.product import Product
from app.models.user import User


class Transaction(Document):
    buyer = ReferenceField(User)
    seller = ReferenceField(User)
    price = IntField()
    product = ReferenceField(Product)
    date_time = DateTimeField()
    quantity = IntField()


