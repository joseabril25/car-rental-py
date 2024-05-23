# user_manager.py
from prettytable import PrettyTable
from models.user import User
from states.global_state import GlobalState
from utils.helpers import hash_password, check_password
from database.engine import DatabaseEngine
from factories.user_factory import UserFactory

class UserManager:
    def __init__(self, current_user=None):
        self.session = DatabaseEngine.get_session()
        self.current_user = current_user

    def register_user(self, fullname, passport, username, password, role="customer"):
        """Registers a new user in the system."""
        
        try:
            # new_user = User(username=username, password=hash_password(password), role=role)
            new_user = UserFactory.create_user(role, username, hash_password(password), fullname, passport)
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

    def get_all_users(self):
        try:
            user = self.session.query(User).all()
            self.display_users(user)
        except Exception as e:
            print(f"Error retrieving available cars: {e}")
            self.session.rollback()
            raise

    def get_user_by_id(self, user_id):
        try:
            user = self.session.query(User).filter(User.user_id == user_id).one()
            return user
        except Exception as e:
            print(f"Error retrieving user: {e}")
            self.session.rollback()
            raise
    
    def delete_user(self, user_id: int):
        try:
            user = self.session.query(User).filter(User.user_id == user_id).one()
            self.session.delete(user)
            self.session.commit()
        except Exception as e:
            print(f"Error deleting user: {e}")
            self.session.rollback()
            raise

    def update_user(self, user_id: int, updated_user: User):
        try:
            user = self.session.query(User).filter(User.user_id == user_id).one()
            if not user:
                print("User not found")
                return False

            UserFactory.update_user(
                user, 
                fullname=updated_user.fullname, 
                passport=updated_user.passport,
                username=updated_user.username,
                password=updated_user.password,
                role=updated_user.role,
                loyalty_points=updated_user.loyalty_points
                )

            self.session.commit()
            self.session.refresh(user)
            return True
        except Exception as e:
            self.session.rollback()
            print(f"Failed to update user: {e}")
            return False
        
    def update_user_loyalty_points(self, user_id: int, points: int):
        try:
            user = self.session.query(User).filter(User.user_id == user_id).one()
            user.loyalty_points += points
            self.session.commit()
            self.session.refresh(user)
        except Exception as e:
            print(f"Error updating user loyalty points: {e}")
            self.session.rollback()
            raise


    def display_users(self, users):
        table = PrettyTable()
        table.field_names = ["User ID", "Full Name","Passport","Username", "User Role", "Loyalty Points"]

        # user: User
        for user in users:
            table.add_row([user.user_id, user.fullname, user.passport, user.username, user.role, user.loyalty_points])

        print(table)
