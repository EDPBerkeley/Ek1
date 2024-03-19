import random
from fastapi import APIRouter, Request, Response

from app.models.transaction import Transaction
from app.utils.db_utils import DBUtils
from app.utils.custom_encoder import custom_serializer


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


    stats = [
        {"stat_name": "Total Revenue (Past 30 Days)", "stat": "$" + str(total_revenue)},
        {"stat_name": "Conversion Rate", "stat": str(random.randint(50, 100)) + "%"},
        {"stat_name": "Customer Satisfaction", "stat": str(random.randint(50, 100)) + "%"},
        {"stat_name": "Most Transacted Product", "stat" : most_transacted_product["name"]},
        {"stat_name": "Highest Earning Product", "stat" : most_revenue_product["name"]},
    ]

    stats_json = json.dumps(stats, cls=custom_serializer)

    return Response(content=stats_json, media_type="application/json")


