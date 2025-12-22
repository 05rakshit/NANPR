import mysql.connector
from mysql.connector import connection

def connect_to_database():
    try:
        cnx = connection.MySQLConnection(
            host="05rakshitgarg.mysql.pythonanywhere-services.com",
            user="05rakshitgarg",
            password="shivaay@",
            database="05rakshitgarg$owner_details"
        )
        return cnx
    except mysql.connector.Error as err:
        print("DB CONNECTION ERROR:", err)
        return None

def get_owner_details(number_plate):
    cnx = connect_to_database()
    if not cnx:
        return None

    cursor = cnx.cursor(dictionary=True) 
    query = "SELECT owner_name, phone_number, Address FROM vehicle_owner WHERE number_plate = %s"
    cursor.execute(query, (number_plate,))
    owner_info = cursor.fetchone()
    cursor.close()
    cnx.close()

    return owner_info
