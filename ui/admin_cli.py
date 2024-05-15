
from factories.user_factory import UserFactory
from managers.cars_manager import CarManager
from managers.rental_manager import RentalManager
from managers.user_manager import UserManager
from models.car import CarType
from states.global_state import GlobalState
from utils.helpers import sanitize_input

class AdminCLI():
    def __init__(self, logout_callback, current_user=None):
        self.user_manager = UserManager()
        self.car_manager = CarManager()
        self.rental_manager = RentalManager()
        self.current_user = current_user
        self.logout_callback = logout_callback

    def admin_dashboard(self):
        while True:
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
                continue
            else:
                print("Invalid option. Please try again.")

    def admin_user_menu(self):
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
        while True:
            print("\nRentals Menu")
            print("1. View Rentals")
            print("2. Approve/Deny Rentals")
            print("3. Update Cars")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.view_all_rentals()
            elif choice == '2':
                self.update_rental_status()
            elif choice == '3':
                # self.update_user()
                self.update_car()
            elif choice == '4':
                self.delete_car()
            elif choice == '5':
                self.admin_dashboard()
            else:
                print("Invalid option. Please try again.")

    
    # USERS METHODS
    def add_user(self):
        username = sanitize_input(input("Enter username: "))
        password = sanitize_input(input("Enter password: "))
        role = input("Enter role (admin/customer): ")
        try:
            self.user_manager.register_user(username, password, role)
            print("User added successfully.")
        except Exception as e:
            print(f"An error occurred during registration: {e}")
    def view_all_users(self):
        try:
            if not self.current_user.is_admin():
                print("You do not have permission to view all users.")
                return
            user_table = self.user_manager.get_all_users()
            print(user_table)
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_user(self):
        try:
            user_id = input("Enter user ID: ")
            self.user_manager.delete_user(user_id)
            print("User deleted successfully.")
        except Exception as e:
            print(f"Failed to delete user: {e}")

    def update_user(self):
        try:
            # Check if user is admin
            if not self.current_user.is_admin():
                print("You do not have permission to view all users.")
                return
            # Get all users and show options
            user_table = self.user_manager.get_all_users()
            print(user_table)

            user_id = int(input("Enter user ID: "))
            #check if user exists
            user = self.user_manager.get_user_by_id(user_id)
            if not user:
                print("User not found.")
                return
            
            # Get new user details
            username = input("Enter new username or press enter to keep: ")
            password = input("Enter new password or press enter to keep: ")
            role = input("Enter new role or press enter to keep (admin/customer): ")

            if username:
                user.username = username
            if password:
                user.password = password
            if role:
                user.role = role

            self.user_manager.update_user(user_id, user)
            print("User updated successfully.")
        except Exception as e:
            print(f"Failed to update user: {e}")


    # CARS METHODS

    def add_car(self):
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        year = input("Enter car year: ")
        mileage = input("Enter car mileage: ")
        plate_number = sanitize_input(input("Enter car plate number: "))
        available_now = input("Is the car available now? (yes/no): ")
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
                available_now = input(f"Is the car available now? (yes/no) or press enter to keep ({car.available_now}): ")

                print("\nChoose a Car Type")
                print("1. Luxury")
                print("2. Economy")
                print("3. SUV")

                car_type_choice = input(f"Enter car type or press enter to keep ({car.car_type.name}): ")

                if car_type_choice.isdigit():
                    car_type = CarType.get_car_type_by_number(car_type_choice)
                else:
                    car_type = car.car_type

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
                    car.car_type = car_type
            
                self.car_manager.update_car(car_id, car)
                print("Car updated successfully.")
                break
            except Exception as e:
                print(f"Failed to add car: {e}")
                break

    def view_available_cars(self):
        try:
            cars = self.car_manager.get_available_cars(self.current_user.is_admin())
            if len(cars) < 1:
                print("No cars available.")
            
            self.car_manager.display_cars(cars)
        except Exception as e:
            print(f"Failed to retrieve available cars: {e}")

    def delete_car(self):
        try:
            car_id = input("Enter car ID: ")
            self.car_manager.delete_car(car_id)
            print("Car deleted successfully.")
        except Exception as e:
            print(f"Failed to delete car: {e}")


    # RENTAL METHODS
    def view_all_rentals(self):
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
        try:
            is_rental_empty = self.view_all_rentals()

            if not is_rental_empty:
                return

            rental_id = input("Enter rental ID: ")
            print('Choose status:')
            print('1. Approve')
            print('2. Reject')
            status = input("Enter status (approved/rejected): ")

            self.rental_manager.update_rental_status(rental_id, status)
        except Exception as e:
            print(f"Failed to retrieve rentals: {e}")