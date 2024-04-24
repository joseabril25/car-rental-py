
class User:
    def __init__(self, user_id, username, hashed_password, role):
        self.user_id = user_id
        self.username = username
        self.hashed_password = hashed_password
        self.role = role

    def is_admin(self):
        return self.role == 'admin'

    def __str__(self):
        return f"User({self.username}, {self.role})"
