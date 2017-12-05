from models.data_base import Data_Base

class Product(Data_Base):
    def __init__(self, id, name, price, type=None, stock=None, description=None):
        super().__init__()
        self.id = id
        self.name = name
        self.price = price
        self.type = type
        self.stock = stock
        self.description = description
        self.insert_product()

    def insert_product(self):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO products (productid, productname, productype, productstock, productprice, productdescription) VALUES (%i, %s, %s, %i, %d, %s)",
            (self.id, self.name, self.type, self.stock, self.price, self.description))
        self.db.commit()

    def get_product_by_id(self):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT productname, productype, productstock, productprice, productdescription FROM products WHERE productid=%i",
            (self.id,))
        return (cursor.fetchone())

    def get_product_by_name(self):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT productname, productype, productstock, productprice, productdescription FROM products WHERE productname=%s",
            (self.name,))
        return (cursor.fetchone())
