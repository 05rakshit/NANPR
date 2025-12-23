import mysql.connector
from mysql.connector import connection

def connect_to_database():
    try:
        cnx = connection.MySQLConnection(
            host = "localhost",
            user = "root",
            password = "admin",
            database = "rakshit"
        )
        return cnx  
    except mysql.connector.Error as err:
        print(err)
        return None

def get_owner_details(number_plate):
    cnx = connect_to_database()
    if cnx:
        cursor = cnx.cursor()
        cursor.execute("SELECT owner_name, phone_number, House_Number, Floor FROM vehicle_owner WHERE number_plate = %s", (number_plate,))
        owner_info = cursor.fetchone()
        cursor.close()
        cnx.close()
        return owner_info
    return None