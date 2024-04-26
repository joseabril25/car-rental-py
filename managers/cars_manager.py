# car_manager.py

from database.db_manager import DBManager
from models.car import Car
from prettytable import PrettyTable

class CarManager:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def add_car(self, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        try:
            query = "INSERT INTO Cars (make, model, year, mileage, available_now, min_rent_period, max_rent_period) VALUES (?, ?, ?, ?, ?, ?, ?)"
            self.db_manager.execute_query(query, (make, model, year, mileage, available_now, min_rent_period, max_rent_period))
        except Exception as e:
            print(f"Error adding car: {e}")
            raise

    def update_car(self, car_id, **kwargs):
        try:
            columns = ', '.join(f"{key} = ?" for key in kwargs)
            values = list(kwargs.values())
            values.append(car_id)
            query = f"UPDATE Cars SET {columns} WHERE car_id = ?"
            self.db_manager.execute_query(query, values)
        except Exception as e:
            print(f"Error updating car: {e}")
            raise

    def delete_car(self, car_id):
        try:
            query = "DELETE FROM Cars WHERE car_id = ?"
            self.db_manager.execute_query(query, (car_id,))
        except Exception as e:
            print(f"Error deleting car: {e}")
            raise

    def get_available_cars(self, is_admin):
        if is_admin:
            query = 'SELECT * FROM Cars'
        else:
            query = 'SELECT * FROM Cars WHERE available_now = 1'
        try:
            cars = self.db_manager.execute_query(query,()).fetchall()
            return [Car(*car) for car in cars]
        except Exception as e:
            print(f"Error retrieving available cars: {e}")
            raise

    def display_cars(self, cars):
        table = PrettyTable()
        table.field_names = ["Car ID", "Make", "Model", "Year", "Mileage", "Status", "Min Rent", "Max Rent"]

        for car in cars:
            availability = "Available" if car.available_now else "Not Available"
            table.add_row([car.car_id, car.make, car.model, car.year, f"{car.mileage} km",
            availability, f"{car.min_rent_period} days", f"{car.max_rent_period} days"])

        print(table)
            