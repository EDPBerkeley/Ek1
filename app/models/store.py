from mongoengine import *

from app.models.product import Product
from app.models.payments_methods import PaymentMethods


class Store(Document):
    name = StringField()
    owner_name = StringField()
    date_created = DateTimeField()
    description = StringField()
    opening_time = IntField()
    closing_time = IntField()
    category = IntField()
    address = StringField()
    location = PointField()
    products = ListField(ReferenceField(Product))
    payment_methods = ListField(IntField())
    website = StringField()
    phone_number = StringField()
    rating = DecimalField(precision=1)
    distance = DecimalField(precision=1)
    cost = IntField()


