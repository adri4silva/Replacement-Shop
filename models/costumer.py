from models.data_base import Data_Base

class Costumer(Data_Base):
    def __init__(self, dni, name, last_name, address, postal_code, t_number, date_birth=None):
        super().__init__()
        self.dni = dni
        self.name = name
        self.last_name = last_name
        self.address = address
        self.postal_code = postal_code
        self.t_number = t_number
        self.date_birth = date_birth

    def insert_costumer(self):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO costumers (dni, costumername, costumerlastname, costumeraddress, costumerpostcode, costumertlfnumber, costumerbirth) VALUES (%s, %s, %s, %s, %i, %i, %s)",
            (self.dni, self.name, self.last_name, self.address, self.postal_code, self.t_number, self.date_birth))
        self.db.commit()
