from models.database import DataBase

class Customer(DataBase):
    """ Customer model.

    This class contains all the necessary methods to access the
    'customers' table in the database.
    """
    def __init__(self, dni, name=None, last_name=None, address=None, postal_code=None, t_number=None, date_birth=None):
        super().__init__()
        self.dni = dni
        self.name = name
        self.last_name = last_name
        self.address = address
        self.postal_code = postal_code
        self.t_number = t_number
        self.date_birth = date_birth

    def insert_customer(self):
        """ Inserts a customer into the database.

        :return: True if the insert was succesful. False otherwise.
        """
        if self.check_user():
            return False
        else:
            cursor = self.db.cursor()
            cursor.execute(
                "INSERT INTO costumers (dni, costumername, costumerlastname, costumeraddress, costumerpostcode, costumertlfnumber, costumerbirth) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (self.dni, self.name, self.last_name, self.address, self.postal_code, self.t_number, self.date_birth))
            self.db.commit()
            return True


    def get_customer(self):
        """ Return the customer row that matches a DNI.

        :return: The costumer row.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT * FROM costumers WHERE dni=?", (self.dni,))
            return cursor.fetchall()
        except:
            print("Error")

    def check_user(self):
        """ Checks if the credentials are correct.

        :return: True if correct. False otherwise.
        """
        try:
            if self.get_customer()[0][0] == self.dni:
                return True
            else:
                return False
        except:
            return False
