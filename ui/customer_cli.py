from factories.user_factory import UserFactory
from managers.cars_manager import CarManager
from managers.rental_manager import RentalManager
from managers.user_manager import UserManager
from models.car import CarType
from states.global_state import GlobalState
from utils.helpers import sanitize_input

class CustomerCLI():
    def __init__(self, logout_callback, current_user=None):
        self.user_manager = UserManager()
        self.car_manager = CarManager()
        self.rental_manager = RentalManager()
        self.current_user = current_user
        self.logout_callback = logout_callback

    def customer_dashboard(self):
        while True:
            print("\nCustomer Dashboard\n")
            print("1. View Cars")
            print("2. Rentals Menu")
            print("3. Account")
            print("4. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                self.view_available_cars()
            if choice == '2':
                print('show rentals menu')
                self.rentals_menu()
            elif choice == '3':
                print('show account')
                # self.view_all_rentals()
            elif choice == '4':
                print(f'Logout successful. Goodbye, {self.current_user.username}!')
                self.logout_callback()
                continue
            else:
                print("Invalid option. Please try again.")

    def rentals_menu(self):
        while True:
            print("\nRentals Menu\n")
            print("1. View Rentals")
            print("2. View Rental Status")
            print("3. Book a Rental")
            print("4. Update Rental Status")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.view_all_rentals()
            if choice == '2':
                print('show rentals menu')
                # self.admin_cars_menu()
            elif choice == '3':
                print('rent a car')
                self.book_rental()
            elif choice == '4':
                print('show account')
                # self.view_all_rentals()
            elif choice == '5':
                print(f'Logout successful. Goodbye, {self.current_user.username}!')
                self.logout_callback()
                continue
            else:
                print("Invalid option. Please try again.")

    def view_available_cars(self):
        try:
            cars = self.car_manager.get_available_cars(self.current_user.is_admin())
            if len(cars) < 1:
                print("No cars available.")
            
            self.car_manager.display_cars(cars)
        except Exception as e:
            print(f"Failed to retrieve available cars: {e}")

    # rental methods
    def view_all_rentals(self):
        try:
            rentals = self.rental_manager.get_all_rentals_by_id(self.current_user.user_id)

            if len(rentals) < 1:
                print("No rentals available.")
            else:
                self.rental_manager.display_rentals(rentals)
        except Exception as e:
            print(f"Failed to retrieve rentals: {e}")

    def book_rental(self):
        cars = self.car_manager.get_available_cars(self.current_user.is_admin())
        if len(cars) < 1:
            print("No cars available.")
        else:
            self.car_manager.display_cars(cars)

            car_id = sanitize_input(input("Enter car ID: "))
            start_date = sanitize_input(input("Enter start date (YYYY-MM-DD): "))
            end_date = sanitize_input(input("Enter end date (YYYY-MM-DD): "))

            try:
                self.rental_manager.create_rental(car_id, self.current_user.user_id, start_date, end_date)
                print("Rental created successfully.")
            except Exception as e:
                print(f"Failed to create rental: {e}")