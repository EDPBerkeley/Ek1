from app.models.product import Product
from app.models.store import Store
from app.models.transaction import Transaction
from app.models.user import User

from app.utils.db_utils import DBUtils as dbu


def clean_db():
    Product.objects().delete()
    Store.objects().delete()
    Transaction.objects().delete()
    User.objects().delete()


dbu.initiate_connection()
clean_db()
