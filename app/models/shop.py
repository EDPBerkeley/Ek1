from mongoengine import *

from models.location import Location
from models.one_image import OneImage
from models.product import Product


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
    banner = EmbeddedDocumentField(OneImage)

