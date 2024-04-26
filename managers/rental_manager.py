# rental_manager.py

from models.rental import Rental
from utils.helpers import validate_date
from database.engine import Session
class RentalManager:
    def __init__(self):
        self.session = Session()

    def create_rental(self, car_id, customer_id, start_date, end_date):
        try:
            validate_date(start_date)
            validate_date(end_date)
            new_rental = Rental(car_id=car_id, user_id=customer_id, start_date=start_date, end_date=end_date)
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
