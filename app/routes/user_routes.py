import json

from fastapi import APIRouter
from fastapi.openapi.models import Response

from models.custom_serializer import CustomSerializer
from utils.custom_encoder import custom_serializer

from utils.db_utils import DBUtils

router = APIRouter()


@router.get("/random_user")
def get_random_user():
    user = DBUtils.get_random_user()
    user_json = json.dumps(user, cls=custom_serializer)
    Response(content=user_json, media_type="application/json")
    return CustomSerializer().to_json(user)
