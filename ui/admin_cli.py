
from factories.user_factory import UserFactory
from managers.cars_manager import CarManager
from managers.rental_manager import RentalManager
from managers.user_manager import UserManager
from models.car import CarType
from models.rental import RentalStatus
from states.global_state import GlobalState
from utils.helpers import hash_password, sanitize_input
import os

class AdminCLI():
    def __init__(self, logout_callback, current_user=None):
        self.user_manager = UserManager()
        self.car_manager = CarManager()
        self.rental_manager = RentalManager()
        self.current_user = current_user
        self.logout_callback = logout_callback

    def admin_dashboard(self):
        os.system('clear')
        is_running = True
        while is_running:
            user = GlobalState.get_current_user()

            print("\nAdmin Dashboard")
            print("1. Users Menu")
            print("2. Cars Menu")
            print("3. Rentals Menu")
            print("4. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                self.admin_user_menu()
            if choice == '2':
                self.admin_cars_menu()
            elif choice == '3':
                self.admin_rental_menu()
            elif choice == '4':
                print(f'Logout successful. Goodbye, {user.username}!')
                self.logout_callback()
                is_running = False
            else:
                print("Invalid option. Please try again.")

    def admin_user_menu(self):
        os.system('clear')
        while True:
            print("\nUsers Menu")
            print("1. Add User")
            print("2. View All Users")
            print("3. Update User")
            print("4. Delete User")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_all_users()
            elif choice == '3':
                self.update_user()
            elif choice == '4':
                self.delete_user()
            elif choice == '5':
                self.admin_dashboard()
            else:
                print("Invalid option. Please try again.")

    def admin_cars_menu(self):
        os.system('clear')
        while True:
            print("\nCars Menu")
            print("1. Add Cars")
            print("2. View All Cars")
            print("3. Update Cars")
            print("4. Delete Cars")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_car()
            elif choice == '2':
                self.view_available_cars()
            elif choice == '3':
                # self.update_user()
                self.update_car()
            elif choice == '4':
                self.delete_car()
            elif choice == '5':
                self.admin_dashboard()
            else:
                print("Invalid option. Please try again.")

    def admin_rental_menu(self):
        os.system('clear')
        is_rental_running = True
        while is_rental_running:
            print("\nRentals Menu")
            print("1. View Rentals")
            print("2. Approve/Deny Rentals")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.view_all_rentals()
            elif choice == '2':
                self.update_rental_status()
            elif choice == '3':
                is_rental_running = False
                continue
            else:
                print("Invalid option. Please try again.")

    
    # USERS METHODS
    def add_user(self):
        os.system('clear')
        fullname = sanitize_input(input("Enter Your Full Name: "))
        passport = sanitize_input(input("Enter Your Passport ID Number: "))
        username = sanitize_input(input("Enter username: "))
        password = sanitize_input(input("Enter password: "))
        role = sanitize_input(input("Enter role (admin/customer): "))

        if role not in ['admin', 'customer']:
            print("Invalid role. Please try again.")
            return
        
        try:
            self.user_manager.register_user(fullname, passport, username, password, role)
            print("User added successfully.")
        except Exception as e:
            print(f"An error occurred during registration: {e}")
    def view_all_users(self):
        os.system('clear')
        try:
            if not self.current_user.is_admin():
                print("You do not have permission to view all users.")
                return
            self.user_manager.get_all_users()
            # print(user_table)
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_user(self):
        try:
            user_id = input("Enter user ID: ")
            confirm = sanitize_input(input("Are you sure you want to delete this user? (yes/no): "))

            if confirm.lower() == 'yes':
                print('Deleting user...')
                self.user_manager.delete_user(user_id)
                print("User deleted successfully.")
        except Exception as e:
            print(f"Failed to delete user: {e}")

    def update_user(self):
        os.system('clear')
        try:
            self.view_all_users()
            
            user_id = int(input("Enter user ID: "))
            #check if user exists
            user = self.user_manager.get_user_by_id(user_id)
            if not user:
                print("User not found.")
                return
            
            # Get new user details
            fullname = sanitize_input(input(f"Enter Your Full Name ({user.fullname}): "))
            passport = sanitize_input(input(f"Enter Your Passport ID Number ({user.passport}): "))
            username = input(f"Enter new username or press enter to keep ({user.username}): ")
            password = input(f"Enter new password or press enter to keep: ")
            role = input(f"Enter new role (admin/customer) or press enter to keep ({user.role}): ")

            if role.strip() and role not in ['admin', 'customer']:
                print("Invalid role. Please try again.")
                return
            if fullname:
                user.fullname = fullname
            if passport:
                user.passport = passport
            if username:
                user.username = username
            if password:
                user.password = hash_password(password)
            if role:
                user.role = role

            self.user_manager.update_user(user_id, user)
            print("User updated successfully.")
        except Exception as e:
            print(f"Failed to update user: {e}")


    # CARS METHODS

    def add_car(self):
        os.system('clear')
        print(f"*** Add New Car *** \n\n")
        make = sanitize_input(input("Enter car make: "))
        model = sanitize_input(input("Enter car model: "))
        year = sanitize_input(input("Enter car year: "))
        mileage = sanitize_input(input("Enter car mileage: "))
        plate_number = sanitize_input(input("Enter car plate number: "))
        available_now = sanitize_input(input("Is the car available now? (yes/no): "))
        print("\nChoose a Car Type")
        print("1. Luxury")
        print("2. Economy")
        print("3. SUV")
        car_type_choice = int(input("Enter car type: "))

        car_type = CarType.get_car_type_by_number(car_type_choice)

        if available_now.lower() == 'yes':
            availability = True
        else:
            availability = False

        try:
            if car_type:
                self.car_manager.add_car(make, model, int(year), int(mileage), plate_number, int(availability), car_type)
                print("Car added successfully.")
        except Exception as e:
            print(f"Failed to add car: {e}")

    def update_car(self):
        os.system('clear')
        print(f"*** Update Car *** \n\n")
        self.view_available_cars()

        while True:
            car_id = input("Enter car ID or type exit: ")

            if car_id.lower() == 'exit':
                print('Exiting update process')
                break

            if not car_id.isdigit():
                print("Invalid input. Please enter a valid numeric car ID.")
                continue
                
            try:
                car = self.car_manager.get_car(int(car_id))

                if not car:
                    print("Car not found.")
                    break
                
                make = input(f"Enter new make or press enter to keep ({car.make}): ")
                model = input(f"Enter new model or press enter to keep ({car.model}): ")
                year = input(f"Enter new year or press enter to keep ({car.year}): ")
                mileage = input(f"Enter new mileage or press enter to keep ({car.mileage}): ")
                plate_number = input(f"Enter new mileage or press enter to keep ({car.plate_number}): ")
                available_now = input(f"Is the car available now? (yes/no) or press enter to keep ({car.available_now}): ")

                print("\nChoose a Car Type")
                print("1. Luxury")
                print("2. Economy")
                print("3. SUV")

                car_type_choice = input(f"Enter car type or press enter to keep ({car.car_type.name}): ")

                if car_type_choice.strip() and CarType.get_car_type_by_number(int(car_type_choice)) is None:
                    print('Invalid car type. Please try again.')
                    return

                if available_now.lower() == 'yes':
                    availability = True
                else:
                    availability = False

                if make:
                    car.make = make
                if model:
                    car.model = model
                if year:
                    car.year = year
                if mileage:
                    car.mileage = mileage
                if available_now:
                    car.available_now = availability
                if car_type_choice:
                    car.car_type = CarType.get_car_type_by_number(int(car_type_choice))
                if plate_number:
                    car.plate_number = plate_number
            
                self.car_manager.update_car(car_id, car)
                print("Car updated successfully.")
                break
            except Exception as e:
                print(f"Failed to add car: {e}")
                break

    def view_available_cars(self):
        os.system('clear')
        print(f"*** View Cars *** \n\n")
        try:
            cars = self.car_manager.get_available_cars(self.current_user.is_admin())
            if len(cars) < 1:
                print("No cars available.")
            
            self.car_manager.display_cars(cars)
        except Exception as e:
            print(f"Failed to retrieve available cars: {e}")

    def delete_car(self):
        os.system('clear')
        print(f"*** Delete Car *** \n\n")
        try:
            self.view_available_cars()
            car_id = input("Enter car ID: ")
            confirm = sanitize_input(input("Are you sure you want to delete this car? (yes/no): "))

            if confirm.lower() == 'yes':
                print('Deleting car...')
                self.car_manager.delete_car(car_id)
                print("Car deleted successfully.")
        except Exception as e:
            print(f"Failed to delete car: {e}")


    # RENTAL METHODS
    def view_all_rentals(self):
        print(f"*** View Rentals *** \n\n")
        os.system('clear')
        try:
            rentals = self.rental_manager.get_all_rentals()

            if len(rentals) < 1:
                print("No rentals available.")
                return False
            else:
                self.rental_manager.display_rentals(rentals)
                return True
        except Exception as e:
            print(f"Failed to retrieve rentals: {e}")

    def update_rental_status(self):
        os.system('clear')
        print(f"*** Update Rental Status *** \n\n")
        try:
            is_rental_empty = self.view_all_rentals()

            if not is_rental_empty:
                return

            rental_id = sanitize_input(input("Enter rental ID: "))

            rental = self.rental_manager.get_rental_by_id(rental_id)

            if not rental:
                print("Rental not found.")
                return
            
            if rental.status == RentalStatus.Done or rental.status == RentalStatus.Cancelled:
                    print(f"Cannot update rental with status {RentalStatus.get_status_name(rental.status)}.")
                    return

            print('Choose status:')
            print('1. Approve')
            print('2. Reject')
            status_choice = input("Enter status (approved/rejected): ")
            if status_choice not in ['1', '2']:
                print("Invalid choice. Please try again.")
                return
            
            status = RentalStatus.get_rental_type_by_number(int(status_choice))

            if status == RentalStatus.Approved:
                car = self.car_manager.get_car(rental.car_id)
                car.available_now = False
            elif status == RentalStatus.Rejected:
                car = self.car_manager.get_car(rental.car_id)
                car.available_now = True

            self.rental_manager.update_rental_status(rental_id, status)
            self.car_manager.update_car(rental.car_id, car)
            print("Rental status updated successfully.")
        except Exception as e:
            print(f"Failed to retrieve rentals: {e}")