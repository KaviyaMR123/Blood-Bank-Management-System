import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Your MySQL username
        password="Kaviya@2003",         # Your MySQL password (empty if none)
        database="eg"        # The DB you just created
    )
