import MySQLdb as data_base
import sqlite3 as db

class DataBase(object):
    """ Database class.
    Connects to the mariaDB database with the credentials.
    """
    def __init__(self):
        self.db = db.Connection("/Users/adri/Proyectos/PycharmProjects/RecambiosCoche/recambios.sqlite")
