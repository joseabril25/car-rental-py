from models.car import Car, CarType
from models.user import User
from utils.helpers import hash_password

INITIAL_DATA = [
    Car(make="Toyota", model="Corolla", year=2020, mileage=15000, plate_number="HFP14", available_now=True, min_rent_period=1, max_rent_period=30, car_type=CarType.Economy, price_per_day=75),
    Car(make="Honda", model="Civic", year=2019, mileage=20000, plate_number="KIL98", available_now=True, min_rent_period=1, max_rent_period=30, car_type=CarType.Economy, price_per_day=75),
    Car(make="Ford", model="Focus", year=2018, mileage=22000, plate_number="MSU89", available_now=True, min_rent_period=3, max_rent_period=45, car_type=CarType.Economy, price_per_day=75),
    Car(make="Chevrolet", model="Malibu", year=2021, mileage=5000, plate_number="SUJ76", available_now=True, min_rent_period=1, max_rent_period=30, car_type=CarType.SUV, price_per_day=100),
    Car(make="Tesla", model="Model 3", year=2022, mileage=10000, plate_number="SSS78", available_now=True, min_rent_period=1, max_rent_period=30, car_type=CarType.Luxury, price_per_day=150),
    User(username="superadmin", password=hash_password("superadmin"), role="admin", fullname="Admin User", passport="SUPERADMIN"),
]

ADMIN_USER = [
    User(username="admin", password=hash_password("admin"), role="admin")
]