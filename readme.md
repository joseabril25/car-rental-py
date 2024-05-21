# Car Rental System

Welcome to the Car Rental System, an easy-to-use platform designed to manage car rentals for both customers and administrators. This system allows for user registration, car management, rental booking, and rental management.

## Getting Started
### Prerequisites
Before you install and run the Car Rental System, make sure you have the following software installed:

* Python 3.9 or later
* pip (Python package installer)
 
### Installation
1. Clone the Repository
```bash
git clone https://github.com/joseabril25/car-rental-py.git
cd car_rental_system
```

2. Create a Virtual Environment
```bash
python -m venv .venv
```

3. Activate the Virtual Environment
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. Install Required Packages
```bash
pip install -r requirements.txt
```

5. Run the Application
```bash
python main.py
```

6. Follow the on-screen instructions to navigate the application.
7. Superadmin credentials:
  * Username: superadmin
  * Password: superadmin

### Configuration
* Database will be created automatically if car_rental_system.db does not exist.
* No additional configuration is required to run the application.

## File Structure

* main.py - The entry point of the application. It handles initialization and starting the command-line interface.
* /models
  * base.py - Contains the SQLAlchemy Base declarative class.
  * car.py - Defines the Car model.
  * user.py - Defines the User model.
  * rental.py - Defines the Rental model.
* /database
  * engine.py - Configures and initializes the database connection and session.
* /managers
  * car_manager.py - Manages car-related operations.
  * user_manager.py - Manages user operations.
  * rental_manager.py - Manages rental operations.
* /factories
  * car_factory.py - Generates Car objects.
  * user_factory.py - Generates User objects.
  * rental_factory.py - Generates Rental objects.
* /utils
  * helpers.py - Contains helper functions for date validation and formatting.
* ui
  * cli.py - Contains the command-line interface for the application.
  * admin_cli.py - Contains the command-line interface for administrators.
  * customer_cli.py - Contains the command-line interface for customers.
* /states
  * global_state.py - Contains the global state of the application.
* /services
  * pricing_service.py - Contains the pricing service for calculating rental prices.
* requirements.txt - Lists all Python packages that need to be installed.
  
## Usage Guide

### Welcome Screen

Upon starting the application, you will be greeted with the welcome screen. From here, you can choose to log in or register as a new user.

1. Login automatically detects if you are an administrator or a customer based on your role.
2. Registration allows you to create a new user account but as a customer.

### Admins

Administrators have access to the following features:

1. User Management:
  * View all users
  * Create users (customers and admins only)
  * Update users (username, password and role)
  * Delete users
2. Car Management:
  * View all cars
  * Create cars
  * Update cars (brand, model, year, and price, etc.)
  * Delete cars
3. Rental Management:
  * View all rentals
  * Approve or Deny rentals
  * Update rentals
  * Delete rentals
  
### Customers

Customers have access to the following features:

1. View available cars
2. Rent cars
  * View customer rentals
  * Book a rental
  * Cancel/Update a rental
3. View profile
  * Update profile


## Licensing
The Car Rental System is released under the MIT License. See the LICENSE file for full license text.

## Known Issues

* Date handling issues when incorrect formats are entered. Ensure dates are always in YYYY-MM-DD format.
* Performance issues with large datasets due to non-optimized queries.

## Credits
Developed by:

Jose Abril Jr. - Initial work and ongoing maintenance

Feel free to contact the developer for any inquiries or support regarding the system.