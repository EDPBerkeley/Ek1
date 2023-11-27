from app.models.product import Product
from app.models.shop import Shop
from app.models.transaction import Transaction
from app.models.user import User

from app.utils.db_utils import DBUtils as dbu
from models.location import Location


def clean_db():
    Product.objects().delete()
    Shop.objects().delete()
    Transaction.objects().delete()
    User.objects().delete()
    Location.objects().delete()


dbu.initiate_connection()
clean_db()