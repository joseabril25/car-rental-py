# user.py

class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password  # In practice, store hashed passwords
        self.role = role  # 'customer' or 'admin'

    def is_admin(self):
        return self.role == 'admin'

    def verify_password(self, password):
        return self.password == password  # This would be more complex with hashing
