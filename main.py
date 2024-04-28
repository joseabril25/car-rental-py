# main.py

from database.engine import DatabaseEngine
from ui.cli import CLI

# def setup_database():
    # Initialize database (only needed once upon first run)
    # init_db()

    # Start a session to perform database operations
    # session = DatabaseEngine.get_session()
    # try:
    #     # Perform some operations
    #     # ...
    #     session.commit()
    # except:
    #     session.rollback()
    #     raise
    # finally:
    #     session.close()

def main():
    """Main function to start the application."""
    print("Setting up the database...")
    # setup_database()
    print("Starting the car rental system...")
    cli = CLI()
    cli.main_menu()

if __name__ == "__main__":
    main()
