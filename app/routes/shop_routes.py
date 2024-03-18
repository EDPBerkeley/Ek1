import base64
import random

from fastapi import APIRouter, Request, Response
from app.models.custom_serializer import CustomSerializer

from app.models.shop import Shop
from utils.custom_encoder import custom_serializer
from utils.db_utils import DBUtils
import json

from models.location import Location

router = APIRouter()

@router.get("/all")
def get_all_stores():
    stores = Shop.objects
    stores_list = [store.to_mongo().to_dict() for store in stores]
    stores_json = json.dumps(stores_list, default=str)
    return stores_json

@router.get("/get_stores")
def get_n_stores(n):
    return Shop.objects()[:n]

@router.get("/random_shop")
def get_random_shop():
    shop = DBUtils.get_random_shop().to_mongo()
    shop1 = DBUtils.get_random_shop()
    binary_data = shop1["sorted_products"]["All Products"][0]["images"][0]["element"].read()
    random_key = random.choice(list(shop1["sorted_products"].keys()))
    binary_data2 = shop1["sorted_products"][random_key][0]["images"][0]["element"].read()
    print(base64.b64encode(binary_data2).decode('utf-8'))
    # print(base64.encode(shop1["sorted_products"]["Cycling"][0]["images"][0]["element"].read()).decode("utf"))

    shop_json = json.dumps(shop, cls=custom_serializer)
    return Response(content=shop_json, media_type="application/json")

@router.get("/get_stores/boundary")
def get_stores_within_boundary(
        request: Request
):
    params = request.query_params
    ne, sw = (float(params["ne_lon"]), float(params["ne_lat"])), (float(params["sw_lon"]), float(params["sw_lat"]))
    # shops = Shop.objects(location__in=Location.objects(geometry__geo_within_box=[ne, sw]))
    shops = Shop.objects(location__geometry__geo_within_box=[ne, sw])
    shops_list = [shop.to_mongo().to_dict() for shop in shops]
    shops_json = json.dumps(shops_list, default=str)

    return shops_json


@router.get("/get_shops/text_search")
def get_shops_text_search(request: Request):
    params = request.query_params

@router.get("/get_shop/shop_id")
def get_shop_given_id(shop_id, resolve_images):
    shop = Shop.objects.get(id=shop_id)
    return CustomSerializer.to_json(shop, resolve_images=bool(int(resolve_images)))



