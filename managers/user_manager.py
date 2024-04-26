# user_manager.py
from models.user import User
from utils.helpers import hash_password, check_password
from database.engine import Session

class UserManager:
    def __init__(self):
        self.session = Session()

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
                # return User(user_id=user_data[0], username=user_data[1], hashed_password=user_data[2], role=user_data[3])  # Return a user object or data tuple
            return None
        except Exception as e:
            print(f"Login failed: {e}")
            self.session.rollback()
            raise

    # def check_user_role(self, username):
    #     try:
    #         query = "SELECT role FROM Users WHERE username = ?"
    #         role = self.db_manager.execute_query(query, (username,)).fetchone()
    #         return role[0] if role else None
    #     except Exception as e:
    #         print(f"Failed to check user role: {e}")
    #         raise
