import os
import random
import secrets
import string
from faker import Faker

from mongoengine import connect

from app.models.payments_methods import PaymentMethods
from app.models.product import Product
from app.models.category import Category
from app.models.store import Store
from app.models.transaction import Transaction
from app.models.user import User


from app.utils.timeutils import TimeUtils
from app.utils.db_utils import DBUtils as dbu

def create_products(delete=False, log=False):
    if delete:
        Product.objects().delete()

    fake = Faker()

    products = []

    for _ in range(20):

        product = Product(
            name=fake.word(),
            description=fake.paragraph(nb_sentences=30),
            price=round(random.uniform(0, 100), 2),
            category=random.randint(0, len(Category.categories) - 1),
            sku=''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(8)),
            quantity=random.randint(0, 199),
            date_created=TimeUtils.random_date_time(5)
        )

        products.append(product)

        try:
            product.save()
            if log:
                print(f"Product {product.id} saved to db")

        except Exception as e:
            print(e)

    return products


def create_payment_methods():
    num_payment_methods = random.randint(0, len(PaymentMethods.payment_methods))
    sample_size = range(len(PaymentMethods.payment_methods))
    payment_methods = random.sample(sample_size, num_payment_methods)
    return payment_methods


def create_stores(delete=False, log=False):
    if delete:
        Store.objects().delete()

    fake = Faker()

    stores = []

    for _ in range(random.randint(1, 2)):
        products = create_products()
        store = Store(
            name=fake.name(),
            date_created=TimeUtils.random_date_time(5),
            description=fake.paragraph(),
            opening_time=random.randint(0, 11),
            closing_time=random.randint(12, 23),
            category=random.randint(0, len(Category.categories)),
            address=fake.address(),
            products=products,
            payment_methods=create_payment_methods()
        )

        stores.append(store)

        try:
            store.save()
            if log:
                print(f"Store {store.id} was saved to db")
        except Exception as e:
            print(e)

    return stores


def create_user(delete=False, log=False):
    if delete:
        User.objects().delete()

    fake = Faker()

    for _ in range(10):

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

    for _ in range(50):
        transaction = Transaction(
            buyer=dbu.get_random_user(),
            seller=dbu.get_random_user(),
            price=round(random.uniform(0, 100), 2),
            product=dbu.get_random_product(),
            date_created=TimeUtils.random_date_time(5),
            quantity=random.randint(0, 10)
        )

        try:
            transaction.save()
            if log:
                print(f"transaction {transaction.id} saved to db")
        except Exception as e:
            print(e)


dbu.initiate_connection()
create_user()
create_transaction(log=True)
