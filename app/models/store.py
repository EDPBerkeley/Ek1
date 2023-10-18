from mongoengine import *

from app.models.product import Product


class Store(Document):
    date_created = DateTimeField()
    description = StringField()
    opening_time = DateTimeField()
    closing_time = DateTimeField()
    category = StringField()
    address = StringField()
    products = ListField(ReferenceField(Product))


