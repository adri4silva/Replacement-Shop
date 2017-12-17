import MySQLdb as data_base

class Data_Base(object):
    """ Database class.
    Connects to the mariaDB database with the credentials.
    """
    def __init__(self):
        self.db = data_base.connect(host="localhost", user="adri", passwd="adrian", db="Recambios")
