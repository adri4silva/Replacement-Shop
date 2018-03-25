import bcrypt
from models.database import DataBase


class User(DataBase):
    """ User model.

    This class contains all the necessary methods to access the
    'users' table in the database.
    """

    def __init__(self, username, password, user_type):
        super().__init__()
        self.username = username
        self.password = password
        self.user_type = user_type

    def password_encryption(self, password):
        """ Converts a password string into a sha256 code.

        :param password: The password string that will be hashed.
        :return: A sha256 code representing the password.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        """ Checks if the given password is the same as the User object's password.

        :param password: A password string.
        :return: True if the passwords are the same. False otherwise.
        """
        return bcrypt.checkpw(password.encode('utf-8'), self.password_encryption(self.password))

    def insert_user(self):
        """ Inserts a user if not exists in the database.

        :return: True if the user is inserted. False otherwise.
        """
        cursor = self.db.cursor()

        if self.get_user() == []:
            cursor.execute("INSERT INTO users (username, password, usertype) VALUES (?, ?, ?)",
                           (self.username, self.password_encryption(self.password), self.user_type))
            self.db.commit()
            return True
        else:
            return False

    def get_user(self):
        """ Checks if the username exists in the database.

        :return: Returns a tuple with the username if exists.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT username FROM users WHERE username=?", (self.username,))
            return cursor.fetchall()
        except:
            print("Error obteniendo usuario")

    def check_user(self):
        """ Checks if the credentials are correct.

        :return: True if correct. False otherwise.
        """
        try:
            if (self.get_user()[0][0] == self.username) and (self.check_password(self.password)):
                return True
            else:
                return False
        except:
            return False
