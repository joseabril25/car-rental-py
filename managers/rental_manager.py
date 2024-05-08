# rental_manager.py

from factories.rental_factory import RentalFactory
from models.rental import Rental
from utils.helpers import validate_date
from database.engine import DatabaseEngine
from prettytable import PrettyTable

class RentalManager:
    def __init__(self):
        self.session = DatabaseEngine.get_session()

    def create_rental(self, car_id, customer_id, start_date, end_date):
        try:
            new_rental = RentalFactory.create_rental(car_id, customer_id, start_date=start_date, end_date=end_date)
            self.session.add(new_rental)
            self.session.commit()
        except Exception as e:
            print(f"Error creating rental: {e}")
            self.session.rollback()
            raise

    def update_rental_status(self, rental_id, status):
        try:
            car = self.session.query(Rental).filter(Rental.rental_id == rental_id).one()
            setattr(car, 'status', status)
            self.session.commit()
        except Exception as e:
            print(f"Error updating rental status: {e}")
            self.session.rollback()
            raise

    def get_all_rentals(self, user_id):
        try:
            return self.session.query(Rental).filter(Rental.user_id == user_id).all()
        except Exception as e:
            print(f'Error fetching all rentals: {e}')
            self.session.rollback()
            raise

    def display_rentals(self, rentals):
        table = PrettyTable()
        table.field_names = ["Rental ID", "Car ID", "User ID", "Start Date", "End Date", "Status"]

        rental: Rental
        for rental in rentals:
            table.add_row([rental.rental_id, rental.car_id, rental.user_id, rental.start_date, rental.end_date, rental.status])

        print(table)
