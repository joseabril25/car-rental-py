from database import DBManager

def setup_database():
    db_manager = DBManager('car_rental_system.db')
    db_manager.create_tables()
    db_manager.close()

if __name__ == "__main__":
    setup_database()
    # Continue with application initialization and main loop
