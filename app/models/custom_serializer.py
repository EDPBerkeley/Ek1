import base64
import copy
import random
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

from mongoengine import *
from bson.objectid import ObjectId
from bson import dbref
from models.location import Location
from models.one_image import OneImage

#
# class CustomSerializer:
#     @staticmethod
#     def to_json(data):
#
#         # Custom logic to recursively resolve ObjectId fields
#         def resolve_object_ids(obj):
#
#             if isinstance(obj, dict):
#                 d = {}
#                 for k, v in obj.items():
#                     d[k] = resolve_object_ids(v)
#                 return d
#             elif isinstance(obj, list):
#                 return [resolve_object_ids(item) for item in obj]
#             elif isinstance(obj, ObjectId):
#                 return str(obj)
#             elif isinstance(obj, ImageGridFsProxy):
#                 obj.seek(0)
#                 binary_data = obj.read()
#                 if (base64.b64encode(binary_data).decode('utf-8') == ""):
#                     print("hit")
#                 return base64.b64encode(binary_data).decode('utf-8')
#             elif isinstance(obj, Document) or isinstance(obj, EmbeddedDocument):
#                 return resolve_object_ids(dict(obj._data))
#             else:
#                 return obj
#
#         return resolve_object_ids(data)

class CustomSerializer:
    @staticmethod
    def to_json(data, resolve_images=False):
        def resolve_and_return_key(k, v, mongoengine_obj):
            # Resolve the object ID and return the key along with the resolved value
            return k, resolve_object_ids(v, mongoengine_obj[k])

        def resolve_object_ids(obj, mongoengine_obj):

            if isinstance(obj, dict) and "_cls" not in obj:

                # d = {}
                # for k, v in obj.items():
                #     d[k] = resolve_object_ids(v, mongoengine_obj[k])

                d = {}
                with ThreadPoolExecutor() as executor:
                    # Submit all tasks to the executor and store the future objects
                    futures = {executor.submit(resolve_and_return_key, k, v, mongoengine_obj): k for k, v in
                               obj.items()}

                    for future in as_completed(futures):
                        k, result = future.result()
                        d[k] = result

                return d
            elif isinstance(obj, list):
                with ThreadPoolExecutor() as executor:
                    results = list(executor.map(resolve_object_ids, obj, mongoengine_obj))
                return results
            elif isinstance(mongoengine_obj, OneImage):
                return CustomSerializer.resolve_image(obj, resolve_image=resolve_images)
            elif isinstance(mongoengine_obj, Document) or isinstance(mongoengine_obj, EmbeddedDocument):
                return resolve_object_ids(dict(mongoengine_obj._data), mongoengine_obj)
            else:
                return str(obj)

        pre_processed_obj = CustomSerializer.pre_process(obj=data)
        serialized_obj = resolve_object_ids(pre_processed_obj, pre_processed_obj)
        post_processed_serialized_obj = CustomSerializer.post_process(obj=serialized_obj)
        return post_processed_serialized_obj

    @staticmethod
    def resolve_image(obj: OneImage, resolve_image=False):
        if resolve_image is True:
            obj.element.thumbnail.seek(0)
            return {
                "url": obj["url"],
                "element": base64.b64encode(obj.element.thumbnail.read()).decode('utf-8')
            }
        else:
            return None


    @staticmethod
    def pre_process(obj):
        copied_obj = copy.deepcopy(obj)
        delattr(copied_obj, 'for_you_products')
        delattr(copied_obj, 'featured_products')
        delattr(copied_obj, 'sorted_products')
        return copied_obj


    @staticmethod
    def post_process(obj: dict) -> dict:
        # Fix the for_you products arr
        for_you_products_copy = copy.deepcopy(obj["products"])
        random.shuffle(for_you_products_copy)
        obj["for_you_products"] = for_you_products_copy

        # Fix the featured_products arr
        featured_products_copy = copy.deepcopy(obj["products"])
        random.shuffle(featured_products_copy)
        obj["featured_products"] = featured_products_copy

        # Add the product_categories arr
        all_product_categories = set()
        sorted_products = defaultdict(list)

        sorted_products["All Products"] = copy.deepcopy(obj["products"])
        for product in obj["products"]:
            all_product_categories.add(product["category"])
            sorted_products[product["category"]].append(product)

        # Add the sorted_products arr
        obj["sorted_products"] = dict(sorted_products)
        obj["product_categories"] = ["All Products"] + list(all_product_categories)

        return obj


