# helpers.py
import re
from datetime import datetime
import bcrypt

def validate_date(date_text):
    """Validate the date format YYYY-MM-DD."""
    try:
        new_date = datetime.strptime(date_text, '%Y-%m-%d').date()
        return new_date
    except ValueError:
        return False

def hash_password(password):
    """Hash a password before storing it in the database."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    """Check that a provided password matches the stored hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def sanitize_input(text):
    """Basic sanitation for text inputs to avoid SQL injection and XSS attacks."""
    return re.sub(r'[^\w\s]', '', text)

def convert_string_to_date(date_string):
    """
    Convert a date string in the format 'YYYY-MM-DD' to a datetime.date object.

    Args:
        date_string (str): The date string to convert.

    Returns:
        datetime.date: The converted date object.
    """
    try:
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    
def check_start_date(date_string):
    """
    Check if the start date is later than today.

    Args:
        start_date (datetime_string): The start date of the rental.

    Returns:
        bool: True if the start date is later than today, False otherwise.
    """
    return datetime.strptime(date_string, '%Y-%m-%d').date() >= datetime.now().date()