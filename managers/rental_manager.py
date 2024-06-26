# rental_manager.py

from factories.rental_factory import RentalFactory
from models.rental import Rental, RentalStatus
from utils.helpers import validate_date
from database.engine import DatabaseEngine
from prettytable import PrettyTable

class RentalManager:
    def __init__(self):
        self.session = DatabaseEngine.get_session()

    def create_rental(self, car, car_id, customer_id, start_date, end_date):
        try:
            new_rental = RentalFactory.create_rental(car=car, car_id=car_id, user_id=customer_id, start_date=start_date, end_date=end_date)
            self.session.add(new_rental)
            self.session.commit()
        except Exception as e:
            print(f"Error creating rental: {e}")
            self.session.rollback()
            raise

    def update_rental_status(self, rental_id, status):
        try:
            rental = self.session.query(Rental).filter(Rental.rental_id == rental_id).one()
            setattr(rental, 'status', status)
            self.session.commit()
        except Exception as e:
            print(f"Error updating rental status: {e}")
            self.session.rollback()
            raise

    def update_rental(self, rental_id, updated_rental: Rental):
        try:
            rental = self.session.query(Rental).filter(Rental.rental_id == rental_id).one()
            RentalFactory.update_rental(rental, start_date=updated_rental.start_date, end_date=updated_rental.end_date)
            self.session.commit()
        except Exception as e:
            print(f"Error updating rental: {e}")
            self.session.rollback()
            raise

    def get_all_rentals(self):
        try:
            return self.session.query(Rental).all()
        except Exception as e:
            print(f'Error fetching all rentals: {e}')
            self.session.rollback()
            raise

    def get_rental_by_id(self, rental_id):
        try:
            return self.session.query(Rental).filter(Rental.rental_id == rental_id).one()
        except Exception as e:
            print(f'Error fetching rental: {e}')
            self.session.rollback()
            raise

    def get_all_rentals_by_user_id(self, user_id):
        try:
            return self.session.query(Rental).filter(Rental.user_id == user_id).all()
        except Exception as e:
            print(f'Error fetching all rentals: {e}')
            self.session.rollback()
            raise

    def display_rentals(self, rentals):
        table = PrettyTable()
        table.field_names = ["Rental ID",  "Car", "Car's Plate Number", "User", "Start Date", "End Date", "Total Cost", "Daily Rate", "Status"]

        rental: Rental
        for rental in rentals:
            car_plate = rental.car.plate_number if rental.car else "No Car"
            car_make = rental.car.make if rental.car else "No Car"
            car_model = rental.car.model if rental.car else "No Car"
            car_year = rental.car.year if rental.car else "No Car"
            car_rate = rental.car.price_per_day if rental.car else "No Car"
            username = rental.user.username if rental.user else "No User"
            status_description = rental.get_status_description()
            table.add_row([
                rental.rental_id, 
                f"{car_make} {car_model} {car_year}",
                car_plate, 
                username, 
                rental.start_date.strftime('%b %d, %Y'), 
                rental.end_date.strftime('%b %d, %Y'), 
                f"${rental.cost}",
                f"${car_rate}",
                status_description
                ])

        print(table)
