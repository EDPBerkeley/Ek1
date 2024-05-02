from mongoengine import *

from models.product import Product
from models.shop import Shop
from models.user import User


class Transaction(Document):
    buyer = ReferenceField(User)
    seller = ReferenceField(User)
    price = DecimalField()
    product = ReferenceField(Product)
    date_created = DateTimeField()
    quantity = IntField()
    shop = ReferenceField(Shop)


