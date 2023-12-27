from fastapi import APIRouter, Request, Response

from models.transaction import Transaction
from utils.db_utils import DBUtils
from utils.custom_encoder import custom_serializer


import json

router = APIRouter()

@router.get("/data")
def overview_data(
        request: Request
):
    params = request.query_params
    shop_id = params["shop_id"]
    transactions = Transaction.objects(shop=shop_id)

    most_transacted_product = DBUtils.calculate_most_bought_product(shop_id=shop_id, transactions=transactions)

    most_revenue_product = DBUtils.calculate_total_revenue_for_product(shop_id=shop_id, transactions=transactions)

    total_revenue = DBUtils.total_revenue(transactions=transactions)


    stats = {
        "most_transacted_product" : most_transacted_product,
        "most_revenue_product" : most_revenue_product,
        "total_revenue" : total_revenue
    }

    stats_json = json.dumps(stats, cls=custom_serializer)

    return Response(content=stats_json, media_type="application/json")


