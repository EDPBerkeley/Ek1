from mongoengine import *

from app.models.product import Product
from app.models.user import User
from models.shop import Shop


class Transaction(Document):
    buyer = ReferenceField(User)
    seller = ReferenceField(User)
    price = DecimalField()
    product = ReferenceField(Product)
    date_created = DateTimeField()
    quantity = IntField()
    shop = ReferenceField(Shop)


