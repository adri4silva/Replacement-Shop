from models.database import DataBase

class Product(DataBase):
    """ Product model.

    This class contains all the necessary methods to access the
    'products' table in the database.
    """
    def __init__(self, id, name=None, type=None, stock=None, price=None, description=None):
        super().__init__()
        self.id = id
        self.name = name
        self.price = price
        self.type = type
        self.stock = stock
        self.description = description

    def insert_product(self):
        """ Inserts a product to the table."""
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO products (productid, productname, productype, productstock, productprice, productdescription) VALUES (?, ?, ?, ?, ?, ?)",
            (self.id, self.name, self.type, self.stock, self.price, self.description))
        self.db.commit()

    def get_product_by_id(self):
        """ Gets the product which matches the given id.

        :return: The product row.
        """
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT productid, productname, productype, productstock, productprice, productdescription FROM products WHERE productid=?",
            (self.id,))
        return (cursor.fetchone())

    def get_product_by_name(self):
        """ Gets the product which matches the given name.

        :return: The product row.
        """
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT productname, productype, productstock, productprice, productdescription FROM products WHERE productname=?",
            (self.name,))
        return (cursor.fetchone())

    def get_products(self):
        """ Gets all the products of the database

        :return: The product row.
        """
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT * FROM products")
        return (cursor.fetchall())

