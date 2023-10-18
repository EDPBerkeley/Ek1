from mongoengine import *


class Product(Document):
    description = StringField()
    price = DecimalField()
    category = IntField()
    sku = StringField()
    inventory = IntField()
    created = DateTimeField()
