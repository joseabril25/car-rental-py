# main.py

from database.engine import DatabaseEngine
from ui.cli import CLI

def main():
    """Main function to start the application."""
    print("Setting up the database...")
    # setup_database()
    print("Starting the car rental system...")
    cli = CLI()
    cli.main_menu()

if __name__ == "__main__":
    main()
