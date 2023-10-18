import os
import random

from mongoengine import connect

from app.models.product import Product
from app.models.user import User

class DBUtils():
    @staticmethod
    def initiate_connection():
        try:
            connect("app", host=os.getenv("MONGODB_URI"))
            print("Connected to db")
        except Exception as e:
            print(e)

    @staticmethod
    def get_random_user():
        num_users = User.objects.count()

        # Generate 5 unique random indices
        random_index= random.sample(range(num_users), 1)[0]

        # Fetch the documents at the random indices
        random_user_list = User.objects.filter().skip(random_index).limit(1)

        return random_user_list[0]

    @staticmethod
    def get_random_product():
        total_products = Product.objects.count()

        # Generate 5 unique random indices
        random_indices = random.sample(range(total_products), 1)

        # Fetch the documents at the random indices
        random_documents = Product.objects.filter().skip(random_indices[0]).limit(1)

        return list(random_documents)[0]