from mongoengine import *
class Location(Document):
    geometry = PointField()
    address = StringField()

    meta = {
        'indexes': [[("location", "2dsphere")]]
    }