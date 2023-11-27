from fastapi import APIRouter

from app.models.shop import Shop
import json

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




