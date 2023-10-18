from mongoengine import *


class Product(Document):
    name = StringField()
    description = StringField()
    price = DecimalField()
    category = IntField()
    sku = StringField()
    quantity = IntField()
    date_created = DateTimeField()
