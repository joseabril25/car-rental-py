import bcrypt

class User:
    def __init__(self, user_id, username, hashed_password, role):
        self.user_id = user_id
        self.username = username
        self.hashed_password = hashed_password
        self.role = role

    def verify_password(self, input_password):
        # Check hashed password
        return bcrypt.checkpw(input_password.encode('utf-8'), self.hashed_password)

    def is_admin(self):
        return self.role == 'admin'

    def __str__(self):
        return f"User({self.username}, {self.role})"
