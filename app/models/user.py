from mongoengine import *

from app.models.product import Product
from app.models.store import Store


class User(Document):
    first_name = StringField()
    last_name = StringField()
    age = StringField()
    location = StringField()
    bio = StringField()
    store = ListField(ReferenceField(Store))
    date_created = DateTimeField()
    cart = ListField(ReferenceField(Product))
    previously_bought = ListField(ReferenceField(Product))



