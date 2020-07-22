import mysql.connector

def dbtester(self):
        dbConnection = mysql.connector.connect(host='localhost',
                                               database='InjectSolar',
                                               user='root',
                                               password='Radha@108')
        cursor = dbConnection.cursor()
        if dbConnection.is_connected():
            db_Info = dbConnection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
        else:
            print("Error while connecting to MySQL")