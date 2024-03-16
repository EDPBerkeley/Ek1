import base64

from fastapi import APIRouter, Request, Response

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.models.shop import Shop
from bson import json_util
import json

from models.product import Product
from utils.custom_encoder import custom_serializer

router = APIRouter()

@router.get("/store")
def get_products_for_store(store_id):


    # return Response(content=json_util.dumps([product.to_mongo().to_dict() for product in Shop.objects(pk=store_id)[0].products]), media_type="application/json")
    # print(products_list)
    # products_json = json_util.dumps(products_list, indent=2)
    # return products_json

    # products = [product.to_mongo() for product in Shop.objects(pk=store_id).first().products]
    products = []
    for product in Shop.objects(pk=store_id).first().products:
        resolved_product=product.to_mongo()
        for i, image in enumerate(product["images"][:1]):
            binary_data = product["images"][i]["element"].read()
            encoded_data = base64.b64encode(binary_data)
            base64_string = encoded_data.decode('utf-8')
            resolved_product["images"][i]["element"] = base64_string
        products.append(resolved_product)
    j = json.dumps(products, cls=custom_serializer)
    return Response(content=j, media_type="application/json")

@router.get("/shop_field")
def get_general_product_field_for_shop(shop_id, product_field):


    # return Response(content=json_util.dumps([product.to_mongo().to_dict() for product in Shop.objects(pk=store_id)[0].products]), media_type="application/json")
    # print(products_list)
    # products_json = json_util.dumps(products_list, indent=2)
    # return products_json

    # products = [product.to_mongo() for product in Shop.objects(pk=store_id).first().products]
    products = []
    for product in Shop.objects(pk=shop_id).first()[product_field]:
        resolved_product=product.to_mongo()
        for i, image in enumerate(product["images"][:1]):
            binary_data = product["images"][i]["element"].read()
            encoded_data = base64.b64encode(binary_data)
            base64_string = encoded_data.decode('utf-8')
            resolved_product["images"][i]["element"] = base64_string
        products.append(resolved_product)
    j = json.dumps(products, cls=custom_serializer)
    return Response(content=j, media_type="application/json")

@router.get("/sorted_products")
def get_sorted_products(shop_id):
    products = {}
    for key, arr in Shop.objects(pk=shop_id).first()["sorted_products"].items():
        curr_products_arr = []
        for product in arr:
            resolved_product=Product.objects.get(id=product).to_mongo()
            product=Product.objects.get(id=product)
            for i, image in enumerate(product["images"][:1]):
                binary_data = product["images"][i]["element"].read()
                encoded_data = base64.b64encode(binary_data)
                base64_string = encoded_data.decode('utf-8')
                resolved_product["images"][i]["element"] = base64_string
            curr_products_arr.append(resolved_product)
        products[key] = curr_products_arr
    j = json.dumps(products, cls=custom_serializer)
    return Response(content=j, media_type="application/json")
