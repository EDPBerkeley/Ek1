from mongoengine import *

from app.models.product import Product
from app.models.payments_methods import PaymentMethods
from models.category import Category
from models.location import Location


class Shop(Document):
    name = StringField()
    owner_name = StringField()
    date_created = DateTimeField()
    description = StringField()
    opening_time = IntField()
    closing_time = IntField()
    category = StringField()
    location = EmbeddedDocumentField(Location)
    address = StringField()
    image = ListField(ReferenceField(Product))
    products = ListField(ReferenceField(Product))
    for_you_products = ListField(ReferenceField(Product))
    featured_products = ListField(ReferenceField(Product))
    sorted_products = DictField(value_field=ListField(ReferenceField(Product)))
    product_categories = ListField(StringField())
    payment_methods = ListField(IntField())
    website = StringField()
    phone_number = StringField()
    rating = DecimalField(precision=1)
    distance = DecimalField(precision=1)
    cost = IntField()


