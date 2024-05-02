import json

from fastapi import APIRouter, Request

from models.custom_serializer import CustomSerializer
from models.product import Product
from models.shop import Shop
from utils.db_utils import DBUtils

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

    return CustomSerializer.to_json(shops, resolve_images=False)


@router.get("/get_shop/shop_id")
def get_shop_given_id(shop_id, resolve_images):
    shop = Shop.objects.get(id=shop_id)
    return CustomSerializer.to_json(shop, resolve_images=bool(int(resolve_images)))


@router.get("/get_shop/text_search")
def get_shops_given_text_search(text_input):
    products_list = Product.objects.search_text(text_input).order_by('$text_score')
    shops = Shop.objects(products__in=products_list)
    return CustomSerializer.to_json(shops, resolve_images=False)
