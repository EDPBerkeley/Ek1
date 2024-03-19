import os
import random
from collections import defaultdict
from mongoengine import connect
from geopy.geocoders import Nominatim

from app.models.product import Product
from app.models.user import User
from app.models.shop import Shop
from app.models.transaction import Transaction


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
    def get_random_shop():
        total_shops = Shop.objects.count()

        # Generate 5 unique random indices
        random_indices = random.sample(range(total_shops), 1)

        # Fetch the documents at the random indices
        random_documents = Shop.objects.filter().skip(random_indices[0]).limit(1)

        return list(random_documents)[0]

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

        return [final_latitude, final_longitude]

    @staticmethod
    def switch_longitude_latitude(coords):
        return[coords[1], coords[0]]

    @staticmethod
    def generate_random_address_berkeley(coords=None):

        geocoder = Nominatim(user_agent="EkBe")

        if coords:
            coords = (str(coords[0]), str(coords[1]))
            return geocoder.reverse(coords)

        coords = DBUtils.generate_random_coords_berkeley()
        str_coords = [str(coords[0]), str(coords[1])]
        return str(geocoder.reverse(str_coords))

    @staticmethod
    def calculate_conversion_rate():
        return random.randint(50, 100)

    @staticmethod
    def calculate_most_bought_product(shop_id, transactions=None):

        if transactions is None:
            transactions = Transaction.objects(shop=shop_id)


        product_id_counts = defaultdict(lambda: 0)
        for transaction in transactions:
            product_id_counts[transaction.product.id] += transaction.quantity

        max_product_id = max(product_id_counts, key=lambda product: product_id_counts[product])
        max_product = DBUtils.get_product(max_product_id)[0].to_mongo()
        return max_product

    @staticmethod
    def calculate_total_revenue_for_product(shop_id, transactions=None):

        if transactions is None:
            transactions = Transaction.objects(shop=shop_id)

        product_ids = [transaction.product.id for transaction in transactions]
        product_id_revenues = defaultdict(lambda: 0)

        for transaction in transactions:
            product_id_revenues[transaction.product.id] += (transaction.quantity * transaction.product.price)

        max_product_revenue_id = max(product_id_revenues, key=lambda product: product_id_revenues[product])
        max_product_revenue = DBUtils.get_product(max_product_revenue_id)[0].to_mongo()

        return max_product_revenue

    @staticmethod
    def total_revenue(transactions=None):

        total_revenue = 0

        for transaction in transactions:
            total_revenue += (transaction.product.price * transaction.quantity)

        return total_revenue



    @staticmethod
    def get_product(product_id):
        return Product.objects(id=product_id)

    @staticmethod
    def get_product_by_name(name):
        return Product.objects(name=name)
