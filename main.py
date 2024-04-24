# main.py

from database.db_manager import DBManager
from ui.cli import CLI

def setup_database():
    """Setup the database and create tables if they don't exist."""
    db_manager = DBManager('car_rental_system.db')
    db_manager.create_tables()
    db_manager.close()

def main():
    """Main function to start the application."""
    print("Setting up the database...")
    setup_database()
    print("Starting the car rental system...")
    cli = CLI()
    cli.main_menu()

if __name__ == "__main__":
    main()
