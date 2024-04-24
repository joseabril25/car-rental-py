# cli.py

from managers.user_manager import UserManager
from managers.cars_manager import CarManager
from managers.rental_manager import RentalManager
from database.db_manager import DBManager
from database.db_manager import DBManager
from models.user import User
from utils.helpers import sanitize_input
from utils.helpers import validate_date

class CLI:
    def __init__(self):
        self.db_manager = DBManager('car_rental_system.db')
        self.user_manager = UserManager(self.db_manager)
        self.car_manager = CarManager(self.db_manager)
        self.rental_manager = RentalManager(self.db_manager)
        self.current_user = None  # Fix: Replace 'User | None' with 'None'
        self.db_manager.create_tables()

    def main_menu(self):
        while True:
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
                break
            else:
                print("Invalid option. Please try again.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            user = self.user_manager.login_user(username, password)
            if user:
                self.current_user = user
                print(f'current user: {self.current_user}')
                print("Login successful.")
                self.user_dashboard()
            else:
                print("Login failed. Please check your credentials.")
        except Exception as e:
            print(f"An error occurred during login: {e}")

    def register(self):
        username = sanitize_input(input("Enter username: "))
        password = sanitize_input(input("Enter password: "))
        role = input("Enter role (admin/customer): ")
        try:
            self.user_manager.register_user(username, password, role)
            print("Registration successful. Please log in.")
        except Exception as e:
            print(f"An error occurred during registration: {e}")

    def user_dashboard(self):
        if self.current_user.is_admin(): # type: ignore
            self.admin_dashboard()
        else:
            self.customer_dashboard()

    def admin_dashboard(self):
        while True:
            print("\nAdmin Dashboard")
            print("1. Add Car")
            print("2. View All Cars")
            print("3. View All Rentals")
            print("4. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_car()
            elif choice == '2':
                self.view_available_cars()
            elif choice == '3':
                self.view_all_rentals()
            elif choice == '4':
                self.logout()
                break
            else:
                print("Invalid option. Please try again.")

    def customer_dashboard(self):
        while True:
            print("\nCustomer Dashboard")
            print("1. View Available Cars")
            print("2. Book a Rental")
            print("3. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                self.view_available_cars()
            elif choice == '2':
                self.book_rental()
            elif choice == '3':
                self.logout()
                break
            else:
                print("Invalid option. Please try again.")

    def add_car(self):
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        year = input("Enter car year: ")
        mileage = input("Enter car mileage: ")
        available_now = input("Is the car available now? (yes/no): ")
        min_rent_period = input("Minimum rental period (days): ")
        max_rent_period = input("Maximum rental period (days): ")
        if available_now.lower() == 'yes':
            availability = 1
        else:
            availability = 0
        try:
            self.car_manager.add_car(make, model, int(year), int(mileage), int(availability), int(min_rent_period), int(max_rent_period))
            print("Car added successfully.")
        except Exception as e:
            print(f"Failed to add car: {e}")

    def view_all_rentals(self):
        try:
            rentals = self.rental_manager.get_all_rentals()
            for rental in rentals:
                print(rental)
        except Exception as e:
            print(f"Failed to retrieve rentals: {e}")

    def view_available_cars(self):
        try:
            cars = self.car_manager.get_available_cars(self.current_user.is_admin())
            if len(cars) < 1:
                print("No cars available.")
            for car in cars:
                print(car)
        except Exception as e:
            print(f"Failed to retrieve available cars: {e}")

    def book_rental(self):
        car_id = input("Enter the car ID: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        try:
            validate_date(start_date)
            validate_date(end_date)
            self.rental_manager.create_rental(car_id, self.current_user.user_id, start_date, end_date)
            print("Rental booked successfully.")
        except Exception as e:
            print(f"Failed to book rental: {e}")

    def logout(self):
        self.current_user = None
        print("Logged out successfully.")
        self.main_menu()

if __name__ == "__main__":
    cli = CLI()
    cli.main_menu()
