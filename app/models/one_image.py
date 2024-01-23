import mongoengine
from mongoengine import ImageField, StringField


class OneImage(mongoengine.EmbeddedDocument):
    element = ImageField(thumbnail_size=(100, 100, True))
    url = StringField()
