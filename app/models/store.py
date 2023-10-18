import mongoengine as db

class Store(db.Document):
    date_created = db.DateTimeField()