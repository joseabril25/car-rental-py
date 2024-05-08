from factories.user_factory import UserFactory
from managers.cars_manager import CarManager
from managers.user_manager import UserManager
from models.car import CarType
from states.global_state import GlobalState
from utils.helpers import sanitize_input

class CustomerCLI():
    def __init__(self, logout_callback, current_user=None):
        self.user_manager = UserManager()
        self.car_manager = CarManager()
        self.current_user = current_user
        self.logout_callback = logout_callback

    def customer_dashboard(self):
        while True:
            print("\nCustomer Dashboard")
            print("1. View Cars")
            print("2. Rentals Menu")
            print("3. Account")
            print("4. Logout")
            choice = input("Choose an option: ")

            if not choice.isdigit():
                print("Invalid option. Please try again.")
                continue

            if choice == 1:
                self.view_available_cars()
            if choice == 2:
                print('show rentals menu')
                # self.admin_cars_menu()
            elif choice == 3:
                print('show account')
                # self.view_all_rentals()
            elif choice == 4:
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