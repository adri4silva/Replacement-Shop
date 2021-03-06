from models.database import DataBase

class Purchase(DataBase):
    """ Purchase model.

    This class contains all the necessary methods to access the
    'purchases' table in the database.
    """
    def __init__(self, dni, productid=None, date=None):
        super().__init__()
        self.dni = dni
        self.productid = productid
        self.date = date

    def get_purchase_by_dni(self):
        """ Gets the purchases that matches the given DNI.

        :return: The purchase row.
        """
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT * FROM purchases WHERE dni=?", (self.dni,))
        return (cursor.fetchall())

    def check_purchase(self):
        try:
            if self.get_purchase_by_dni()[0][0] == self.dni:
                return True
            else:
                return False
        except:
            return False

