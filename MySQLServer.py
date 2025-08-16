import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="password"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
        return None

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()