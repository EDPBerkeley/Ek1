from fastapi import APIRouter

from app.models.store import Store
import json

router = APIRouter()

@router.get("/all")
def get_all_stores():
    stores = Store.objects
    stores_json = [store.to_json() for store in stores]
    return stores_json

@router.get("/get_stores")
def get_n_stores(n):
    return Store.objects()[:n]




