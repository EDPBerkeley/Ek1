import os
import random
import mongoengine as db
from datetime import datetime, timedelta

from mongoengine import connect

from app.main import client

from app.models.store import Store


def create_stores():
    connect("app", host=os.getenv("MONGODB_URI"))

    Store.objects().delete()

    # Define the range of the last 5 years (in days)
    start_date = datetime.now() - timedelta(days=365 * 5)
    end_date = datetime.now()

    for _ in range(20):  # You can specify the number of random dates you want
        random_days = random.randint(0, (end_date - start_date).days)
        random_date = start_date + timedelta(days=random_days)

        store = Store(date_created=random_date)

        try:
            store.save()
            print(f"store '{store.id}' saved to db")

        except Exception as e:
            print(e)


create_stores()
