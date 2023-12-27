from fastapi import APIRouter, Request, Response

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
    print(shop)
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
    print(shops)
    shops_list = [shop.to_mongo().to_dict() for shop in shops]
    shops_json = json.dumps(shops_list, default=str)
    return shops_json





