from mongoengine import *
class Location(Document):
    coordinates = PointField()
    address = StringField()

    meta = {
        'indexes': [[("location", "2dsphere")]]
    }