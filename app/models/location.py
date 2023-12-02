from mongoengine import *
class Location(EmbeddedDocument):
    geometry = PointField()
    address = StringField()

    meta = {
        'indexes': [[("location", "2dsphere")]]
    }