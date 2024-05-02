import copy
import random
from collections import defaultdict

import dbu

from models.product import Product
from models.shop import Shop

"""
    This script is meant to populate the sorted products dictionary with real data, for_you products array with
    dummy data, featured_products array with dummy data, and create the categories_list array with real data
    
    Due to the fact that this is a migration there will be no mongoengine objects being dealt with and every single
    db object is going to be treated as a python dict with _id NOT id
"""


# For each product call a func that will mutate the shop and save it to the db
def re_populate_shop(shop: Shop) -> dict:


    # Fix the for_you products arr
    for_you_products_copy = copy.deepcopy(shop.products)
    random.shuffle(for_you_products_copy)
    shop.for_you_products = for_you_products_copy

    # Fix the featured_products arr
    featured_products_copy = copy.deepcopy(shop.products)
    random.shuffle(featured_products_copy)
    shop.featured_products = featured_products_copy

    # Add the product_categories arr
    all_product_categories = set()
    sorted_products = defaultdict(list)

    product_collection = Product._get_collection()
    sorted_products["All Products"] = copy.deepcopy(shop["products"])
    for product in copy.deepcopy(shop["products"]):
        # product_object = Product.objects.get(id=product_object_id)
        all_product_categories.add(product.category)
        sorted_products[product.category].append(product)


    # Add the sorted_products arr
    shop.sorted_products = dict(sorted_products)
    shop.product_categories = ["All Products"] + list(all_product_categories)

    return shop




def main():


    # Instantiate the db
    dbu.initiate_connection()


    shop_collection = Shop._get_collection()
    shop_collection.update_many({}, {'$set': {'for_you_products': []}})
    shop_collection.update_many({}, {'$set': {'featured_products': []}})
    shop_collection.update_many({}, {'$set': {'product_categories': []}})
    shop_collection.update_many({}, {'$set': {'sorted_products': {}}})

    product_collection = Product._get_collection()
    product_collection.update_many({}, {'$set': {''}})

    # Product: {
    #     "images": [
    #         {
    #             "element": ObjectID(),
    #             "url": string
    #         }
    #     ]
    # }

    for shop in Shop.objects.all():

        re_populate_shop(shop)

        try:
            shop.save()
            print(f"Shop {shop.id} has been saved to db")
        except Exception as e:
            print(f"Could not save shop {shop.id} to db because of {e}")


if __name__ == "__main__":
    main()
