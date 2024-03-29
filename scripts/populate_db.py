import json
import os
import random
import secrets
import string
import os
import time
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
from PIL import Image
import io

from app.utils.timeutils import TimeUtils
from app.utils.db_utils import DBUtils as dbu
from models.location import Location
from models.one_image import OneImage


def load_data():
    global data
    global PRODUCTS
    with open('../assets/data.json', 'r') as json_file:
        data = json.load(json_file)

    with open("../assets/stripped_products_2.json") as product_file:
        PRODUCTS = json.load(product_file)


def create_images(product_name, shop_category):

    directory = f"/Users/erchispatwardhan/PycharmProjects/fastApiProject/assets/{product_name}"
    os.makedirs(directory, exist_ok=True)
    images = []

    for j in range(2):

        time.sleep(12)

        # prompt = f"I need a prompt that is less than 1000 in length to give dalle - I want to generate an image of {product_name} that is only a simple near-white background as if it were taken in a photography studio. I want this image to be used in a advertising catalogue, and I want the whole object in frame. Please respond with just the prompt"

        # text_response = client.chat.completions.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "user", "content": prompt},
        #     ]
        # )

        # text_prompt = text_response.choices[0].message.content

        text_prompt =  f"I need a well-shot and edited studio-like photo of a single {product_name} taking into consideration the fact that it in an instance of {shop_category} shot on a white background that would be used in an advertising catalogue to showcase the product and can you make sure that the entire product is visible in the frame of the picture?"

        try:
            image_response = client.images.generate(
                model="dall-e-3",
                prompt=text_prompt,
                size="1024x1024",
                quality="standard",
                n=1,
                response_format="url",
                
            )
        except Exception as e:
            print(e + " caused by " + text_prompt)

        image_url = image_response.data[0].url


        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                image = Image.open(io.BytesIO(response.content))
                compressed_image_io = io.BytesIO()
                image.save(compressed_image_io, 'JPEG', quality=85)
                compressed_image_data = compressed_image_io.getvalue()
                # Save Image
                image_path = f"{directory}/{product_name}_{j}.jpg"
                with open(image_path, 'wb') as f:
                    f.write(compressed_image_data)

                images.append(
                    OneImage(
                        element=BytesIO(compressed_image_data),
                        url=image_url
                    )
                )

        except requests.RequestException as e:
            print(f"Error downloading {image_url}: {e}")

    return images


def create_products(shop_num, num_products, shop_category, delete=False, log=True):
    if delete:
        Product.objects().delete()

    products = []



    for i in range(num_products):

        product_subcategory_num = random.randint(0, len(PRODUCTS[shop_num]["product_subcategories"]) - 1)
        product_subcategory = PRODUCTS[shop_num]["product_subcategories"][product_subcategory_num]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role" : "system", "content" : "For every output please only responsd in json format that I will specify in the conversation"},
                {"role" : "user", "content" : f"Given the product category {product_subcategory} please output a json containing a realistic product name, "
                                              f"product description, a realistic price without the dollar sign (i.e. - just the number) for it and a realistic quantity that a store would have of that product"
                                              f" please respond with a json with the keys, name, description, price, and quantity please respond with just the json - nothing else at all"}
            ],
            response_format={ "type": "json_object" }
        )
        product_details = json.loads(response.choices[0].message.content)



        try:
            product = Product(
                name=product_details["name"],
                description=product_details["description"],
                price=product_details["price"],
                category=product_subcategory,
                sku=''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(8)),
                quantity=product_details["quantity"],
                date_created=TimeUtils.random_date_time(5),
                images=create_images(product_name=product_details["name"], shop_category=shop_category)
            )


            products.append(product)

            product.save()
            if log:
                print(f"Product {product_details['name']} with _id {product.id} saved to db")

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


def create_stores(delete=False, log=False):
    if delete:
        Shop.objects().delete()

    fake = Faker()

    shops = []

    for i in range(1):

        location = create_location()
        shop_num = random.randint(0, len(PRODUCTS) - 1)
        shop_category = PRODUCTS[shop_num]["shop_category"]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role" : "system", "content" : "For every output please only responsd in json format that I will specify in the conversation"},
                {"role" : "user", "content" : f"Give the shop category {shop_category} please output a json containing a realistic shop name, shop description, and a shop website"
                                              f"please respond in the format "
                                              f"{{"
                                              f"\"name\" : \"shop_name_that_chat_gpt_chooses\", "
                                              f"\"description\" : \"shop_description_that_chat_gpt_chooses\""
                                              f"\"website\" : \"shop_website_that_chat_gpt_chooses\""
                                              f"}}"}
            ],
            response_format={ "type": "json_object" }
        )
        shop_details = json.loads(response.choices[0].message.content)

        for_you = create_products(shop_num=shop_num, num_products=8, shop_category=shop_category)
        featured = create_products(shop_num=shop_num, num_products=8, shop_category=shop_category)
        products = create_products(shop_num=shop_num, num_products=14, shop_category=shop_category)

        curr_shop = Shop(
            name= shop_details["name"],
            owner_name = fake.name(),
            date_created=TimeUtils.random_date_time(5),
            description=shop_details["description"],
            opening_time=random.randint(0, 11),
            closing_time=random.randint(12, 23),
            category=shop_category,
            location=location,
            for_you = for_you,
            featured = featured,
            products=products,
            payment_methods=create_payment_methods(),
            website=shop_details["website"],
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

    for i in range(10):

        stores = create_stores()
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
