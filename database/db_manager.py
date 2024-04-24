# db_manager.py

import sqlite3

class DBManager:
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.conn = None

    def connect(self):
        """Establish a database connection."""
        self.conn = sqlite3.connect(self.db_filename)
        return self.conn

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        """Execute a database query."""
        if not self.conn:
            self.connect()
        cur = self.conn.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        self.conn.commit()
        return cur

    def create_tables(self):
        """Create database tables based on the schema."""
        with open('database/schema.sql', 'r') as f:
            schema = f.read()
        self.execute_query(schema)
