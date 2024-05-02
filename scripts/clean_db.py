from utils.db_utils import DBUtils as dbu


from models.product import Product
from models.shop import Shop
from models.transaction import Transaction
from models.user import User


def clean_db():
    Product.objects().delete()
    Shop.objects().delete()
    Transaction.objects().delete()
    User.objects().delete()


dbu.initiate_connection()
clean_db()