from werkzeug.security import generate_password_hash, check_password_hash

users = []

class User:
    user_id = 1

    def __init__(self, username, password, firstname, lastname, email=None, phonenumber=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phoneNumber = phonenumber
        self.username = username
        self.password = User.hash_password(password)

        User.user_id += 1

    @staticmethod
    def find_by_name(username):
        for user in users:
            if user.username == username:
                return user
        return None

    @staticmethod
    def find_by_id(user_id):
        for user in users:
            if user.id == user_id:
                return user
        return None

    @classmethod
    def hash_password(cls, clear_password):
        if clear_password:
            return generate_password_hash(clear_password)

        return None

    def authenticated(self, password=''):
        return check_password_hash(self.password, password)

    def save_to_db(self):
        users.append(self)
