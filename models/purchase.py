from models.data_base import Data_Base

class Purchase(Data_Base):
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
            "SELECT * FROM purchases WHERE dni=%s", (self.dni,))
        return (cursor.fetchone())

