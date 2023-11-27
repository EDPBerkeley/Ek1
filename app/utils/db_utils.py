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

    @staticmethod
    def generate_random_n_digit_number(n):
        if n < 1:
            raise ValueError("Number of digits must be at least 1")
        lower_bound = 10 ** (n - 1)
        if n == 1:
            upper_bound = 9  # 10^1 - 1 is 9 for a single-digit number
        else:
            upper_bound = (10 ** n) - 1
        return random.randint(lower_bound, upper_bound)

    @staticmethod
    def generate_random_coords_berkeley():
        rand_latitude = DBUtils.generate_random_n_digit_number(7)
        rand_longitude = DBUtils.generate_random_n_digit_number(7)

        str_latitude = "37.8" + str(rand_latitude)
        str_longitude = "-122.2" + str(rand_longitude)

        final_latitude, final_longitude = float(str_latitude), float(str_longitude)

        return final_latitude, final_longitude

