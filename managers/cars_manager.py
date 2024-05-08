# car_manager.py

from database.engine import DatabaseEngine
from models.car import Car
from prettytable import PrettyTable
from factories.car_factory import CarFactory
from services.pricing_service import PricingService

class CarManager:
    def __init__(self):
        self.session = DatabaseEngine.get_session()

    def add_car(self, make, model, year, mileage, available_now, car_type):
        try:
            new_car = CarFactory.create_or_update_car(
                car_type=car_type, 
                make=make, 
                model=model, 
                year=year, 
                mileage=mileage, 
                available_now=available_now)
            
            print('new_car: ', new_car)
            self.session.add(new_car)
            self.session.commit()
        except Exception as e:
            print(f"Error adding car: {e}")
            self.session.rollback()
            raise

    def update_car(self, car_id, updated_car: Car):
        try:
            car = self.session.query(Car).filter(Car.car_id == car_id).one()
            
            CarFactory.create_or_update_car(
                car=car, 
                car_type=updated_car.car_type,
                make=updated_car.make, 
                model=updated_car.model, 
                year=updated_car.year, 
                mileage=updated_car.mileage, 
                available_now=updated_car.available_now)
            
            self.session.commit()

        except Exception as e:
            print(f"Error updating car: {e}")
            self.session.rollback()
            raise

    def delete_car(self, car_id):
        try:
            car = self.session.query(Car).filter(Car.car_id == car_id).one()
            self.session.delete(car)
            self.session.commit()
        except Exception as e:
            print(f"Error deleting car: {e}")
            self.session.rollback()
            raise

    def get_available_cars(self, is_admin):
        try:
            if is_admin:
                return self.session.query(Car).all()
            return self.session.query(Car).filter(Car.available_now == True).all()
        except Exception as e:
            print(f"Error retrieving available cars: {e}")
            self.session.rollback()
            raise

    def get_car(self, car_id) -> Car:
        try:
            return self.session.query(Car).filter(Car.car_id == car_id).one()
        except Exception as e:
            print(f"Error retrieving car: {e}")
            self.session.rollback()
            raise

    def display_cars(self, cars):
        table = PrettyTable()
        table.field_names = ["Car ID", "Make", "Model", "Year", "Mileage", "Status", "Min Rent", "Max Rent", "Type", "Daily Rate"]

        for car in cars:
            availability = "Available" if car.available_now else "Not Available"
            table.add_row([car.car_id, car.make, car.model, car.year, f"{car.mileage} km",
            availability, f"{car.min_rent_period} days", f"{car.max_rent_period} days", car.car_type.name, f"${PricingService.get_daily_rate(car.car_type)}"])

        print(table)
            