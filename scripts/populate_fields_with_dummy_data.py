import random
from collections import defaultdict

from app.utils.db_utils import DBUtils as dbu
from models.shop import Shop

"""
    This script is meant to populate the sorted products dictionary with real data, for_you products array with
    dummy data, featured_products array with dummy data, and create the categories_list array with real data
"""


# For each product call a func that will mutate the shop and save it to the db
def re_populate_shop(shop: Shop) -> None:
    # Fix the for_you products arr
    for_you_products_copy = shop.products.all()
    random.shuffle(for_you_products_copy)
    shop.for_you_products = for_you_products_copy

    # Fix the featured_products arr
    featured_products_copy = shop.products.all()
    random.shuffle(featured_products_copy)
    shop.featured_products = featured_products_copy

    # Add the product_categories arr
    all_products_categories = set()
    sorted_products = defaultdict(list)

    for product in shop.products:
        all_products_categories.add(product.category)
        sorted_products[product.category].append(product)

    # Add the sorted_products arr
    shop.sorted_products = sorted_products
    shop.product_categories = list(all_products_categories)
    shop.save()


def main():
    # Instantiate the db
    dbu.initiate_connection()

    # Import all shops and fill in their products
    shops = Shop.objects.all()
    for shop in shops:
        re_populate_shop(shop)


if __name__ == "__main__":
    main()
