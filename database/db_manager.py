# db_manager.py

import sqlite3
from sqlite3 import Error

class DBManager:
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.conn = None

    def connect(self):
        """Establish a database connection."""
        try:
            self.conn = sqlite3.connect(self.db_filename)
            print("Connection to SQLite DB successful")
            return self.conn
        except Error as e:
            print(f"Failed to connect to SQLite database: {e}")
            raise

    def close(self):
        """Close the database connection."""
        try:
            if self.conn:
                self.conn.close()
                print("Connection to SQLite DB closed")
        except Error as e:
            print(f"Failed to close the SQLite database connection: {e}")
            raise

    def execute_query(self, query, params=None):
        """Execute a standard database query."""
        try:
            if not self.conn:
                self.connect()
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            if 'SELECT' not in query.upper():
                self.conn.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Database query failed: {e}")
            raise
    
    def execute_script(self, script_path):
        """Execute a script containing multiple SQL statements."""
        try:
            if not self.conn:
                self.connect()
            cursor = self.conn.cursor()
            with open(script_path, 'r') as sql_file:
                sql_script = sql_file.read()
            cursor.executescript(sql_script)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error executing script: {e}")
            raise

    def create_tables(self):
        """Create database tables based on the schema."""
        try:
            with open('database/schema.sql', 'r') as f:
                schema = f.read()
            self.execute_query(schema)
            print("Database tables created successfully")
        except IOError as e:
            print(f"Unable to read schema file: {e}")
            raise
        except Error as e:
            print(f"Failed to execute schema: {e}")
            raise
