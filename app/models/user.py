import mongoengine as db

from app.models.store import Store

class User(db.Document):
    first_name = db.StringField()
    last_name = db.StringField()
    age = db.StringField()
    location = db.StringField()
    bio = db.StringField()
    store = db.ReferenceField(Store)
    date_created = db.DateTimeField()



