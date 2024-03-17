from mongoengine import *
from models.one_image import OneImage
from models.custom_serializer import CustomSerializer


class Product(Document, CustomSerializer):
    name = StringField()
    description = StringField()
    price = DecimalField()
    category = StringField()
    sku = StringField()
    quantity = IntField()
    date_created = DateTimeField()
    images = EmbeddedDocumentListField(OneImage)

    meta = {
        'indexes': [
            {
                'fields': ['$name', "$description", "$category"],
                'default_language': 'en',
                'weights': {
                    'name': 4,
                    'description': 10,
                    'category': 4
                }
            }
        ]
    }

    def to_json(self):
        return CustomSerializer.to_json(self)

