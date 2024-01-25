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
        for i, image in enumerate(product["images"]):
            binary_data = product["images"][i]["element"].read()
            encoded_data = base64.b64encode(binary_data)
            base64_string = encoded_data.decode('utf-8')
            resolved_product["images"][i]["element"] = base64_string
        products.append(resolved_product)
    j = json.dumps(products, cls=custom_serializer)
    return Response(content=j, media_type="application/json")
