import mysql.connector

def dbtester(self):
        dbConnection = mysql.connector.connect(host='localhost',
                                               database='InjectSolar',
                                               user='root',
                                               password='Radha@108')
        cursor = dbConnection.cursor()
        if dbConnection.is_connected():
            sqldb_Info = dbConnection.get_server_info()
            print("MySQL Server version ", sqldb_Info)
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
        else:
            print("Not able to connect")
