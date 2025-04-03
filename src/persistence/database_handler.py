# src/persistence/database_handler.py

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

class DatabaseHandler:
    def __init__(self):
        """
        Initializes the database connection using credentials from environment variables.
        """
        load_dotenv()  # Load environment variables from .env file
        self.host = os.getenv('DB_HOST')
        self.database = os.getenv('DB_DATABASE')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.connection = None

    def connect(self):
        """
        Establishes the connection to the MySQL database.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Database connected successfully.")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None

    def close(self):
        """
        Closes the database connection.
        """
        if self.connection and self.connection.is_connected():
            try:
                self.connection.close()
            except Exception as e:
                print(f"Error closing the connection: {e}")

    def execute_query(self, query, params=None):
        """
        Executes a query that does not return results (INSERT, UPDATE, DELETE).
        """
        if self.connection and self.connection.is_connected():
            cursor = self.connection.cursor()
            try:
                cursor.execute(query, params)
                self.connection.commit()
            except Error as e:
                print(f"Error while executing query: {e}")
            finally:
                cursor.close()

    def fetch_results(self, query, params=None):
        """
        Executes a SELECT query and fetches the results.
        """
        results = []
        if self.connection and self.connection.is_connected():
            cursor = self.connection.cursor()
            try:
                cursor.execute(query, params)
                results = cursor.fetchall()
            except Error as e:
                print(f"Error while fetching results: {e}")
            finally:
                cursor.close()
        return results
