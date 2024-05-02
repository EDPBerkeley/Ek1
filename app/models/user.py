from mongoengine import *

from models.product import Product
from models.shop import Shop


class User(Document):
    first_name = StringField()
    last_name = StringField()
    age = IntField()
    bio = StringField()
    stores = ListField(ReferenceField(Shop))
    date_created = DateTimeField()
    cart = ListField(ReferenceField(Product))
    previously_bought = ListField(ReferenceField(Product))
