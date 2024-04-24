# customer.py

class Customer:
    def __init__(self, customer_id, name, license_number):
        self.customer_id = customer_id
        self.name = name
        self.license_number = license_number

    def get_customer_info(self):
        return f"{self.name}, License No: {self.license_number}"
