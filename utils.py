import mysql.connector
from mysql.connector import connection

# Initialize EasyOCR once (faster performance)
# reader = easyocr.Reader(['en'], gpu=False)

def connect_to_database():
    try:
        cnx = connection.MySQLConnection(
            user='root', 
            password='QHdpjQYeAqWdLwnuIQPcwPwrHBcCwJFY', 
            host='mainline.proxy.rlwy.net', 
            database='railway', 
            port='55270'
        )
        return cnx
    except mysql.connector.Error as err:
        print(err)
        return None

def get_owner_details(number_plate):
    cnx = connect_to_database()
    if cnx:
        cursor = cnx.cursor()
        cursor.execute("SELECT owner_name, phone_number, address FROM vehicle_owner WHERE number_plate = %s", (number_plate.upper(),))
        owner_info = cursor.fetchone()
        cursor.close()
        cnx.close()
        return owner_info
    return None