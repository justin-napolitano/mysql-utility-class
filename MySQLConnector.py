import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

class MySQLConnector:
    def __init__(self):
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.host = os.getenv('DB_HOST')
        self.database = os.getenv('DB_NAME')
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host
                # Do not specify database here
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Connected to MySQL server")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")

    def create_database(self, database_name):
        try:
            self.cursor.execute(f"CREATE DATABASE {database_name}")
            self.cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
            result = self.cursor.fetchone()
            if result:
                print(f"Database {database_name} created successfully")
                return True
            else:
                print(f"Database {database_name} was not created")
                return False
        except Error as e:
            print(f"Error while creating database: {e}")
            return False
        
    def drop_database(self, database_name):
        try:
            self.cursor.execute(f"DROP DATABASE {database_name}")
            self.cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
            result = self.cursor.fetchone()
            if not result:
                print(f"Database {database_name} dropped successfully")
                return True
            else:
                print(f"Database {database_name} was not dropped")
                return False
        except Error as e:
            print(f"Error while dropping database: {e}")
            return False


    def use_database(self,database_name):
        try:
            self.cursor.execute(f"USE {database_name}")
            print(f"Using database {database_name}")
        except Error as e:
            print(f"Error while selecting database: {e}")

    def execute_script_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                sql_script = file.read()
            
            sql_commands = sql_script.split(';')
            for command in sql_commands:
                if command.strip():
                    self.cursor.execute(command)
                    print(f"Executed: {command}")
            self.connection.commit()
            print("SQL script executed successfully")
        except Error as e:
            print(f"Error while executing SQL script: {e}")


# Usage example
if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    db_name = 'testing_db'
    db = MySQLConnector()
    db.connect()
    db.create_database(db_name)  # Replace 'new_database' with the desired database name
    db.use_database(db_name)  # Use the specified database from .env
    db.drop_database(db_name)
    db.disconnect()
