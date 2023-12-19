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

    k = [product.to_mongo() for product in Shop.objects(pk=store_id).first().products]
    j = json.dumps(k, cls=custom_serializer)
    return Response(content=j, media_type="application/json")
