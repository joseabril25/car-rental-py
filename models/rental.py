# rental.py

class Rental:
    def __init__(self, rental_id, car, customer, start_date, end_date):
        self.rental_id = rental_id
        self.car = car
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date

    def extend_rental(self, new_end_date):
        self.end_date = new_end_date

    def calculate_cost(self):
        days = (self.end_date - self.start_date).days
        return self.car.calculate_rental_cost(days)
