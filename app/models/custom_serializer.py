import base64
import copy
import random
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from mongoengine import *

from models.one_image import OneImage
from models.product import Product
from models.shop import Shop


class CustomSerializer:
    """
    def umbrella method

        def gen_serializer

            if
            elif
            elif
            elif

        def shop(mongoengine doc)
            preprocess(obj)
            gen_serializer(obj)
            post_p
    """

    @staticmethod
    def to_json(obj, resolve_images=False):

        def serialize_general_object(obj, mongoengine_obj):

            if isinstance(obj, dict) and "_cls" not in obj:

                d = {}
                for k, v in obj.items():
                    d[k] = serialize_general_object(v, mongoengine_obj[k])
                return d
            elif isinstance(obj, list) or isinstance(obj, QuerySet):
                with ThreadPoolExecutor() as executor:
                    results = list(executor.map(serialize_general_object, obj, mongoengine_obj))
                return results
            elif isinstance(mongoengine_obj, OneImage):
                return serialize_image(obj)
            elif isinstance(obj, Product):
                return serialize_product(obj)
            elif isinstance(obj, Shop):
                return serialize_shop(obj)
            elif isinstance(mongoengine_obj, Document) or isinstance(mongoengine_obj, EmbeddedDocument):
                return serialize_general_object(dict(mongoengine_obj._data), mongoengine_obj)
            else:
                return str(obj)

        def serialize_product(product: Product):
            def pre_process_product(product_doc: Product) -> Product:
                product_dict = dict(product_doc._data)
                keys_subset, keys_to_delete = Product._fields.keys(), set()
                for k, _ in product_dict.items():
                    if k not in keys_subset:
                        keys_to_delete.add(k)
                for key in keys_to_delete: del product_dict[key]
                return Product(**product_dict)

            preprocessed_product = pre_process_product(product_doc=product)
            serialized_product = serialize_general_object(obj=dict(preprocessed_product._data), mongoengine_obj=preprocessed_product)
            return serialized_product


        def serialize_shop(shop: Shop):

            def pre_process_shop(shop_doc: Shop):
                copied_obj = copy.deepcopy(shop_doc)
                delattr(copied_obj, 'for_you_products')
                delattr(copied_obj, 'featured_products')
                delattr(copied_obj, 'sorted_products')
                return copied_obj

            def post_process_shop(shop_dict: dict) -> dict:
                # Fix the for_you products arr
                for_you_products_copy = copy.deepcopy(shop_dict["products"])
                random.shuffle(for_you_products_copy)
                shop_dict["for_you_products"] = for_you_products_copy

                # Fix the featured_products arr
                featured_products_copy = copy.deepcopy(shop_dict["products"])
                random.shuffle(featured_products_copy)
                shop_dict["featured_products"] = featured_products_copy

                # Add the product_categories arr
                all_product_categories = set()
                sorted_products = defaultdict(list)

                sorted_products["All Products"] = copy.deepcopy(shop_dict["products"])
                for product in shop_dict["products"]:
                    all_product_categories.add(product["category"])
                    sorted_products[product["category"]].append(product)

                # Add the sorted_products arr
                shop_dict["sorted_products"] = dict(sorted_products)
                shop_dict["product_categories"] = ["All Products"] + list(all_product_categories)

                return shop_dict

            pre_processed_obj = pre_process_shop(shop_doc=shop)
            serialized_obj = serialize_general_object(dict(pre_processed_obj._data), pre_processed_obj)
            post_processed_serialized_obj = post_process_shop(shop_dict=serialized_obj)
            return post_processed_serialized_obj

        def serialize_image(img: OneImage):
            if resolve_images is True:
                img.element.seek(0)
                return {
                    "url": img["url"],
                    "element": base64.b64encode(img.element.read()).decode('utf-8')
                }
            else:
                return "Unserialized Image"

        return serialize_general_object(obj=obj, mongoengine_obj=obj)
