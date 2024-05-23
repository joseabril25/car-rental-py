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

    # def admin_dashboard(self):
    #     while True:
    #         user = GlobalState.get_current_user()
    #         print('user: ', user)
    #         print("\nAdmin Dashboard")
    #         print("1. Users Menu")
    #         print("2. Cars Menu")
    #         print("3. Rentals Menu")
    #         print("4. Logout")
    #         choice = input("Choose an option: ")

    #         if choice == '1':
    #             self.admin_user_menu()
    #         if choice == '2':
    #             self.add_car()
    #         elif choice == '3':
    #             self.view_all_rentals()
    #         elif choice == '4':
    #             self.logout()
    #             break
    #         else:
    #             print("Invalid option. Please try again.")

    # def admin_user_menu(self):
    #     while True:
    #         print("\nUser Menu")
    #         print("1. Add User")
    #         print("2. View All Users")
    #         print("3. Update User")
    #         print("4. Delete User")
    #         print("5. Exit")
    #         choice = input("Choose an option: ")

    #         if choice == '1':
    #             self.add_car()
    #         elif choice == '2':
    #             self.admin_cli.view_all_users()
    #         elif choice == '3':
    #             self.view_all_rentals()
    #         elif choice == '4':
    #             self.view_all_rentals()
    #         elif choice == '5':
    #             self.admin_dashboard()
    #         else:
    #             print("Invalid option. Please try again.")

    # def customer_dashboard(self):
    #     while True:
    #         print("\nCustomer Dashboard")
    #         print("1. View Available Cars")
    #         print("2. Book a Rental")
    #         print("3. Logout")
    #         choice = input("Choose an option: ")

    #         if choice == '1':
    #             self.view_available_cars()
    #         elif choice == '2':
    #             self.book_rental()
    #         elif choice == '3':
    #             self.logout()
    #             break
    #         else:
    #             print("Invalid option. Please try again.")

    # def add_car(self):
    #     make = input("Enter car make: ")
    #     model = input("Enter car model: ")
    #     year = input("Enter car year: ")
    #     mileage = input("Enter car mileage: ")
    #     available_now = input("Is the car available now? (yes/no): ")
    #     print("\nChoose a Car Type")
    #     print("1. Luxury")
    #     print("2. Economy")
    #     print("3. SUV")
    #     car_type_choice = int(input("Enter car type: "))

    #     car_type = CarType.get_car_type_by_number(car_type_choice)

    #     if available_now.lower() == 'yes':
    #         availability = True
    #     else:
    #         availability = False

    #     try:
    #         if car_type:
    #             self.car_manager.add_car(make, model, int(year), int(mileage), int(availability), car_type)
    #             print("Car added successfully.")
    #     except Exception as e:
    #         print(f"Failed to add car: {e}")

    # def view_all_rentals(self):
    #     try:
    #         rentals = self.rental_manager.get_all_rentals()
    #         if len(rentals) < 1:
    #             print(f'No Rentals Available')
            
    #         self.rental_manager.display_rentals(rentals)
    #     except Exception as e:
    #         print(f"Failed to retrieve rentals: {e}")

    

    # def book_rental(self):
    #     car_id = input("Enter the car ID: ")
    #     start_date = input("Enter start date (YYYY-MM-DD): ")
    #     end_date = input("Enter end date (YYYY-MM-DD): ")
    #     try:
    #         validate_date(start_date)
    #         validate_date(end_date)
    #         self.rental_manager.create_rental(int(car_id), self.current_user.user_id, start_date, end_date)
    #         print("Rental booked successfully.")
    #     except Exception as e:
    #         print(f"Failed to book rental: {e}")

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
