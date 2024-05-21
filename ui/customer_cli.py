from factories.rental_factory import RentalFactory
from managers.cars_manager import CarManager
from managers.rental_manager import RentalManager
from managers.user_manager import UserManager
from models.rental import Rental, RentalStatus
from utils.helpers import check_start_date, convert_string_to_date, sanitize_input, validate_date
import os


class CustomerCLI():
    def __init__(self, logout_callback, current_user=None):
        self.user_manager = UserManager()
        self.car_manager = CarManager()
        self.rental_manager = RentalManager()
        self.current_user = current_user
        self.logout_callback = logout_callback

    def customer_dashboard(self):
        os.system('clear')
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
                self.view_account()
            elif choice == '4':
                print(f'Logout successful. Goodbye, {self.current_user.username}!')
                self.logout_callback()
                continue
            else:
                print("Invalid option. Please try again.")

    def rentals_menu(self):
        os.system('clear')
        while True:
            print("\nRentals Menu\n")
            print("1. View Rentals")
            print("2. Book a Rental")
            print("3. Update Rental")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.view_all_rentals()
            elif choice == '2':
                self.book_rental()
            elif choice == '3':
                self.update_rental()
            elif choice == '4':
                self.customer_dashboard()
                continue
            else:
                print("Invalid option. Please try again.")

    # user methods
    def view_account(self):
        os.system('clear')
        print(f"Full Name: {self.current_user.fullname}")
        print(f"Passport ID Number: {self.current_user.passport}")
        print(f"Username: {self.current_user.username}")
        print(f"Role: {self.current_user.role}")

    # car methods
    def view_available_cars(self):
        os.system('clear')
        try:
            cars = self.car_manager.get_available_cars(self.current_user.is_admin())
            if len(cars) < 1:
                print("No cars available.")
            
            self.car_manager.display_cars(cars)
        except Exception as e:
            print(f"Failed to retrieve available cars: {e}")

    # rental methods
    def view_all_rentals(self):
        os.system('clear')
        try:
            rentals = self.rental_manager.get_all_rentals_by_user_id(self.current_user.user_id)

            if len(rentals) < 1:
                print("No rentals available.")
            else:
                self.rental_manager.display_rentals(rentals)
        except Exception as e:
            print(f"Failed to retrieve rentals: {e}")

    def book_rental(self):
        os.system('clear')
        cars = self.car_manager.get_available_cars(self.current_user.is_admin())
        if len(cars) < 1:
            print("No cars available.")
        else:
            self.car_manager.display_cars(cars)

            car_id = sanitize_input(input("Enter car ID: "))
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")

            try:
                car = self.car_manager.get_car(car_id)
                if not car:
                    print("Car not found.")
                    return
                
                if not validate_date(start_date) or not validate_date(end_date):
                    print("Invalid date format.")
                    return
                
                # check if start_date is later than date today
                if not check_start_date(start_date):
                    print("Start date must be later than today.")
                    return
                
                calculate_price = RentalFactory.calculate_cost(start_date, end_date, car.price_per_day)
                print(f"Cost: ${calculate_price}")
                confirm = input("Confirm booking? (yes/no): ")
                if confirm.lower() != 'yes':
                    os.system('clear')
                    print("Booking canceled.")
                    return
                
                self.rental_manager.create_rental(car, car_id, self.current_user.user_id, start_date, end_date)
                print("Rental created successfully.")
            except Exception as e:
                print(f"Failed to create rental: {e}")

    def update_rental(self):
        os.system('clear')
        try:
            rentals = self.rental_manager.get_all_rentals_by_user_id(self.current_user.user_id)
            if len(rentals) < 1:
                print("No cars available.")
            else:
                self.rental_manager.display_rentals(rentals)

                rental_id = sanitize_input(input("Enter Rental ID: "))

                rental = self.rental_manager.get_rental_by_id(rental_id)
                if not rental:
                    print("Rental not found.")
                    return
                
                if rental.status == RentalStatus.Approved or rental.status == RentalStatus.Rejected or rental.status == RentalStatus.Done or rental.status == RentalStatus.Cancelled:
                    print(f"Cannot update rental with status {RentalStatus.get_status_name(rental.status)}.")
                    return
                
                cancel = input(f"Cancel rental? (yes/no): ")

                if (cancel.lower() == 'yes'):
                    self.rental_manager.update_rental_status(rental_id, RentalStatus.Cancelled)
                    print("Rental canceled successfully.")
                    return

                start_date = input(f"Enter new start date (YYYY-MM-DD) or press enter to keep ({rental.start_date}): ")
                end_date = input(f"Enter new end date (YYYY-MM-DD) or press enter to keep ({rental.end_date}): ")
                

                if start_date and not validate_date(start_date):
                    print("Invalid start date format.")
                    return
                if end_date and not validate_date(end_date):
                    print("Invalid end date format.")
                    return
                
                if start_date:
                    rental.start_date = convert_string_to_date(start_date)
                if end_date:
                    rental.end_date = convert_string_to_date(end_date)
                
                self.rental_manager.update_rental(rental_id, rental)
                print("Rental updated successfully.")
        except Exception as e:
            print(f"Failed to create rental: {e}")