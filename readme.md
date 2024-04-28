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

2. Install Required Packages
```bash
pip install -r requirements.txt
```
3. Initialize the Database
```bash
python -m database.engine
```

4. Run the Application
```bash
python main.py
```

### Configuration
* Database Configuration: Configure the database by editing the DATABASE_URL in database/engine.py to point to your preferred database.
* Environment Variables: Set up necessary environment variables for a production environment, such as FLASK_ENV for Flask applications.

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
* requirements.txt - Lists all Python packages that need to be installed.

## Licensing
The Car Rental System is released under the MIT License. See the LICENSE file for full license text.

## Known Issues

* Date handling issues when incorrect formats are entered. Ensure dates are always in YYYY-MM-DD format.
* Performance issues with large datasets due to non-optimized queries.

## Credits
Developed by:

Jose Abril Jr. - Initial work and ongoing maintenance

Feel free to contact the developer for any inquiries or support regarding the system.