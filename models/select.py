from models.data_base import Data_Base
from models.user import User

class Select(Data_Base):
    def __init__(self):
        super().__init__()

    def check_user(self, username, password):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT username, password FROM users WHERE username=%s and password=%s",
            (username, User.password_encryption(User, password)))
        return (cursor.fetchone())

    def get_sales(self, username):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT productid, transactiondate FROM sales WHERE username=%s",
            (username,))
        return (cursor.fetchone())

    def get_purchases(self, dni):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT productid, transactiondate FROM purchases WHERE dni=%s",
            (dni,))
        return (cursor.fetchone())
