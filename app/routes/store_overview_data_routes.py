from fastapi import APIRouter, Request, Response

from utils.db_utils import DBUtils

router = APIRouter()

@router.get("/data")
def overview_data(
        request: Request
):
    params = request.query_params
    shop_id = params["shop_id"]
    max_product = DBUtils.calculate_most_bought_product(shop_id)
    return max_product


