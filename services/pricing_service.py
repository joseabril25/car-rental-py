from models.car import CarType

# 
class PricingService:
    _pricing_per_day = {
        CarType.Luxury: 150,   # $150 per day for luxury cars
        CarType.Economy: 75,   # $75 per day for economy cars
        CarType.SUV: 100       # $100 per day for SUVs
    }

    @staticmethod
    def get_daily_rate(car_type):
        return PricingService._pricing_per_day.get(car_type, 0) # Return 0 if car type not found