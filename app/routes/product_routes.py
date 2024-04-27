from fastapi import APIRouter

from app.models.shop import Shop
from app.models.product import Product
from app.models.custom_serializer import CustomSerializer


router = APIRouter()

@router.get("/store")
def get_products_for_store(store_id):

    return CustomSerializer.to_json(Shop.objects(pk=store_id).first().products, resolve_images=True)


@router.get("/shop_field")
def get_general_product_field_for_shop(shop_id, product_field):

    general_products = Shop.objects(pk=shop_id).first()[product_field]
    general_products_json = CustomSerializer.to_json(general_products, resolve_images=True)
    return general_products_json



@router.get("/text_search")
def get_product_by_text_search(text_input):
    products = Product.objects.search_text(text_input).order_by('$text_score')
    products_json = [CustomSerializer.to_json(product) for product in products]
    return products_json

