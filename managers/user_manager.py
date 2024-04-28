# user_manager.py
from models.user import User
from utils.helpers import hash_password, check_password
from database.engine import DatabaseEngine

class UserManager:
    def __init__(self):
        self.session = DatabaseEngine.get_session()

    def register_user(self, username, password, role):
        try:
            new_user = User(username=username, password=hash_password(password), role=role)
            self.session.add(new_user)
            self.session.commit()
        except Exception as e:
            print(f"Failed to register user: {e}")
            self.session.rollback()
            raise

    def login_user(self, username, password) -> User:
        try:
            user = self.session.query(User).filter(User.username == username).one_or_none()
            if user and check_password(password, user.password):
                return user
            return None
        except Exception as e:
            print(f"Login failed: {e}")
            self.session.rollback()
            raise
