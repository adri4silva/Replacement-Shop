import MySQLdb as data_base
import sqlite3 as db

class Data_Base(object):
    """ Database class.
    Connects to the mariaDB database with the credentials.
    """
    def __init__(self):
        self.db = db.Connection("/Users/adri/Proyectos/PycharmProjects/RecambiosCoche/recambios.sqlite")
