import json
import os
import random
import secrets
import string
import os
from io import BytesIO

import requests
from openai import OpenAI
from faker import Faker

from mongoengine import *

from app.models.payments_methods import PaymentMethods
from app.models.product import Product
from app.models.category import Category
from app.models.shop import Shop
from app.models.transaction import Transaction
from app.models.user import User


from app.utils.timeutils import TimeUtils
from app.utils.db_utils import DBUtils as dbu
from models.location import Location
from models.one_image import OneImage


def load_data():
    global data
    with open('../assets/data.json', 'r') as json_file:
        data = json.load(json_file)


def create_images(product_name):

    directory = f"/Users/erchispatwardhan/PycharmProjects/fastApiProject/assets/{product_name}"
    os.makedirs(directory, exist_ok=True)
    images = []

    for j in range(2):
        prompt = f"I need a prompt that is less than 1000 in length to give dalle - I want to generate an image of {product_name} that is only a simple near-white background as if it were taken in a photography studio. I want this image to be used in a advertising catalogue, and I want the whole object in frame. Please respond with just the prompt"

        text_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ]
        )

        text_prompt = text_response.choices[0].message.content

        try:
            image_response = client.images.generate(
                model="dall-e-2",
                prompt=text_prompt,
                size="512x512",
                quality="standard",
                n=1,
            )
        except Exception as e:
            print(text_prompt)

        image_url = image_response.data[0].url

        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                # Save Image
                image_path = f"{directory}/{product_name}_{j}.jpg"
                with open(image_path, 'wb') as f:
                    f.write(response.content)

                images.append(
                    OneImage(
                        element=BytesIO(response.content),
                        url=image_url
                    )
                )

        except requests.RequestException as e:
            print(f"Error downloading {image_url}: {e}")

    return images


def create_products(shop_num, delete=False, log=True):
    if delete:
        Product.objects().delete()

    products = []

    for i, curr_product in enumerate(data[shop_num]["products"]):



        try:
            product = Product(
                name=curr_product["name"],
                description=curr_product["description"],
                price=round(random.uniform(0, 100), 2),
                category=curr_product["category"],
                sku=''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(8)),
                quantity=random.randint(0, 199),
                date_created=TimeUtils.random_date_time(5),
                images=create_images(product_name=curr_product["name"])
            )


            products.append(product)

            product.save()
            if log:
                print(f"Product {curr_product['name']} with _id {product.id} saved to db")

        except Exception as e:
            print(e)

    return products


def create_payment_methods():
    num_payment_methods = random.randint(0, len(PaymentMethods.payment_methods))
    sample_size = range(len(PaymentMethods.payment_methods))
    payment_methods = random.sample(sample_size, num_payment_methods)
    return payment_methods

def create_location(delete=False, log=False):
    if delete:
        Location.objects().delete()

    coords = dbu.generate_random_coords_berkeley()
    address = dbu.generate_random_address_berkeley(coords)[0]

    location = Location(
        geometry={'type': 'Point', 'coordinates': dbu.switch_longitude_latitude(coords)},
        address=address
    )
    try:
        location.validate()
    except Exception as e:
        print(e)

    return location


def create_stores(user_num, delete=False, log=False):
    if delete:
        Shop.objects().delete()

    fake = Faker()

    shops = []

    shop_num_left_bound = user_num * 2
    for i, shop in enumerate(data[shop_num_left_bound:shop_num_left_bound + 2]):
        products = create_products(shop_num=shop_num_left_bound + i)
        location = create_location()

        curr_shop = Shop(
            name= shop["name"],
            owner_name = fake.name(),
            date_created=TimeUtils.random_date_time(5),
            description=shop["description"],
            opening_time=random.randint(0, 11),
            closing_time=random.randint(12, 23),
            category=shop["category"],
            location=location,
            products=products,
            payment_methods=create_payment_methods(),
            website=shop["website"],
            phone_number=str(fake.numerify(text='###')) + '-' + str(fake.numerify(text='###')) + "-" + str(fake.numerify(text='####')),
            rating=format(round(random.uniform(0, 6), 1), ".1f"),
            distance=format(round(random.uniform(0, 6), 1), ".1f"),
            cost=round(random.uniform(1, 3))
        )

        shops.append(curr_shop)

        try:
            curr_shop.save()
            if log:
                print(f"Shop {curr_shop.id} was saved to db")
        except Exception as e:
            print(e)

    return shops


def create_user(delete=False, log=False):
    if delete:
        User.objects().delete()

    fake = Faker()

    for i in range(4, 10):

        stores = create_stores(user_num=i)
        user = User(
            first_name=fake.name(),
            last_name=fake.name(),
            age=random.randint(0, 70),
            bio=fake.paragraph(nb_sentences=30),
            stores=stores,
            date_created=TimeUtils.random_date_time(5),
            cart=[dbu.get_random_product() for _ in range(random.randint(0, 5))],
            previously_bought=[dbu.get_random_product() for _ in range(random.randint(0, 5))]
        )

        try:
            user.save()
            if log:
                print(f"user {user.id} saved to db")
        except Exception as e:
            print(e)


def create_transaction(delete=False, log=False):
    if delete:
        Transaction.objects().delete()

    for _ in range(400):
        transaction = Transaction(
            buyer=dbu.get_random_user(),
            seller=dbu.get_random_user(),
            price=round(random.uniform(0, 100), 2),
            product=dbu.get_random_product(),
            date_created=TimeUtils.random_date_time(5),
            quantity=random.randint(1, 10),
            shop=dbu.get_random_shop()
        )

        try:
            transaction.save()
            if log:
                print(f"transaction {transaction.id} saved to db")
        except Exception as e:
            print(e)


dbu.initiate_connection()
client = OpenAI()
load_data()
create_user()
create_transaction(log=False)







# Example usage
# First, create and save a Location instance
# dbu.initiate_connection()
# def create():
#
#     location = Location(coordinates={'type': 'Point', 'coordinates': [-73.935242, 40.730610]})
#     location.save()
#     return location
#
# t = create()
# # Now, create and save a Place instance that references the Location
# store = Store(name="Central Park", location=t)
# store.save()
