# cli.py

from database.engine import DatabaseEngine
from factories.user_factory import UserFactory
from managers.user_manager import UserManager
from managers.cars_manager import CarManager
from managers.rental_manager import RentalManager
from models.user import User
from models.car import CarType
from states.global_state import GlobalState
from ui.admin_cli import AdminCLI
from ui.customer_cli import CustomerCLI
from utils.helpers import sanitize_input
from utils.helpers import validate_date
import os
import sys

class CLI:
    def __init__(self):
        self.user_manager = UserManager()
        self.car_manager = CarManager()
        self.rental_manager = RentalManager()
        self.current_user = None  # Fix: Replace 'User | None' with 'None'
        self.admin_cli = AdminCLI(logout_callback=self.main_menu)
        self.customer_cli = CustomerCLI(logout_callback=self.main_menu)
        self.session = DatabaseEngine.get_session()

    def main_menu(self):
        is_running = True
        os.system('clear')
        while is_running:
            print("\nWelcome to the Car Rental System")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.login()
            elif choice == '2':
                self.register()
            elif choice == '3':
                print("Exiting system.")
                is_running = False
                sys.exit()
            else:
                print("Invalid option. Please try again.")

    def login(self): 
        os.system('clear')
        print(f"*** User Login *** \n\n")
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            user = self.user_manager.login_user(username, password)
            if user:
                self.current_user = user
                GlobalState.set_current_user(user)
                self.user_manager.current_user = user
                print(f'\n\nLogin successful.')
                self.user_dashboard(user)
            else:
                print(f'\n\nLogin failed. Please check your credentials.\n\n')
        except Exception as e:
            print(f"An error occurred during login: {e}")

    def register(self):
        os.system('clear')
        print(f"*** User Registration *** \n\n")

        fullname = sanitize_input(input("Enter Your Full Name: "))
        passport = sanitize_input(input("Enter Your Passport ID Number: "))
        username = sanitize_input(input("Enter Your Username: "))
        password = sanitize_input(input("Enter Your Password: "))
        try:
            self.user_manager.register_user(fullname, passport, username, password)
            print("Registration successful. Please log in.")
        except Exception as e:
            print(f"An error occurred during registration: {e}")

    def user_dashboard(self, user):
        if self.current_user.is_admin(): # type: ignore
            self.admin_cli.current_user = user
            self.admin_cli.admin_dashboard()
        else:
            self.customer_cli.current_user = user
            self.customer_cli.customer_dashboard()

    def logout(self):
        os.system('clear')
        self.current_user = None
        GlobalState.logout()
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
        finally:
            self.session.expire_all()
            self.session.close()
            self.session = DatabaseEngine.get_session()
        print("Logged out successfully.")
        self.main_menu()

if __name__ == "__main__":
    cli = CLI()
    cli.main_menu()
