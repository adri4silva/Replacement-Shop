import MySQLdb as data_base

class Data_Base(object):
    def __init__(self):
        self.db = data_base.connect(host="localhost", user="adri", passwd="adrian", db="Recambios")
