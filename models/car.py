# car.py

class Car:
    def __init__(self, car_id, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available_now = available_now
        self.min_rent_period = min_rent_period
        self.max_rent_period = max_rent_period

    def get_details(self):
        details = f"{self.year} {self.make} {self.model}, Mileage: {self.mileage}km"
        availability = "Available" if self.available_now else "Not Available"
        return f"{details}, {availability}"
