import json
from fastapi import APIRouter, Response

from app.utils.custom_encoder import custom_serializer
from app.utils.db_utils import DBUtils

router = APIRouter()

@router.get("/random_user")
def get_random_user():
    user = DBUtils.get_random_user().to_mongo()
    user_json = json.dumps(user, cls=custom_serializer)
    return Response(content=user_json, media_type="application/json")