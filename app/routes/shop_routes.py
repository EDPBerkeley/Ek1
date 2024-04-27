import base64
import random
import json
from fastapi import APIRouter, Request, Response

from app.models.custom_serializer import CustomSerializer
from app.models.shop import Shop
from app.utils.custom_encoder import custom_serializer
from app.utils.db_utils import DBUtils
from models.product import Product

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
    return CustomSerializer.to_json(shop, resolve_images=True)


@router.get("/get_stores/boundary")
def get_stores_within_boundary(
        request: Request
):
    params = request.query_params
    ne, sw = (float(params["ne_lon"]), float(params["ne_lat"])), (float(params["sw_lon"]), float(params["sw_lat"]))
    shops = Shop.objects(location__geometry__geo_within_box=[ne, sw])
    # shops_list = [shop.to_mongo().to_dict() for shop in shops]
    # shops_json = json.dumps(shops_list, default=str)


    return CustomSerializer.to_json(shops, resolve_images=False)


@router.get("/get_shops/text_search")
def get_shops_text_search(request: Request):
    params = request.query_params


@router.get("/get_shop/shop_id")
def get_shop_given_id(shop_id, resolve_images):
    shop = Shop.objects.get(id=shop_id)
    return CustomSerializer.to_json(shop, resolve_images=bool(int(resolve_images)))


@router.get("/get_shop/text_search")
def get_shops_given_text_search(text_input):
    products_list = Product.objects.search_text(text_input).order_by('$text_score')
    shops = Shop.objects(products__in=products_list)
    return CustomSerializer.to_json(shops, resolve_images=False)


