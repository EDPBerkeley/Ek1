from mongoengine import *

from app.models.product import Product
from app.models.payments_methods import PaymentMethods
from models.location import Location


class Shop(Document):
    name = StringField()
    owner_name = StringField()
    date_created = DateTimeField()
    description = StringField()
    opening_time = IntField()
    closing_time = IntField()
    category = IntField()
    location = EmbeddedDocumentField(Location)
    address = StringField()
    products = ListField(ReferenceField(Product))
    payment_methods = ListField(IntField())
    website = StringField()
    phone_number = StringField()
    rating = DecimalField(precision=1)
    distance = DecimalField(precision=1)
    cost = IntField()


