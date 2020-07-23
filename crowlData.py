import requests
import mysql.connector

class crowel:

    def login_req(self):
        global authotoken
        url = "http://3.6.0.2/inject-solar-angular/inject_solar_server/admin/Admin/login"
        login_cred = {"login_id": "triose", "password": "triose123"}
        login_resp = requests.post(url, json=login_cred)
        resp_json = login_resp.json()

        # add response object from the website to get the token
        token = resp_json["resultObject"]["token"]
        authotoken= {"Authorization": token}

    def elct_generation(self):
        url = "http://3.6.0.2/inject-solar-angular/inject_solar_server/normal/Normal/getDashboardData"
        elecGen = requests.get(url, headers=authotoken)
        # fetching the result object data from the dashboard
        tGenRes = elecGen.json()
        tGendata = tGenRes["resultObject"]["totalTodayEnergyGenerated"]
        print("Today's Energy Generation: ", tGendata)

    def errorlogs(self):
        global logdata
        url= "http://3.6.0.2/inject-solar-angular/inject_solar_server/normal/Alarms/getClearedNormalAlarms"
        param = {"user_id": "90", "start_date": "2020-01-01", "end_date": "2020-02-29", "limit": "10", "offset": "0"}
        elogs = requests.post(url, headers=authotoken, json=param)
        elogsdata = elogs.json()
        logdata = elogsdata['resultObject']

    def sqlload_data(self):

        dbConnection = mysql.connector.connect(host='localhost',
                                               database='InjectSolar',
                                               user='root',
                                               password='Radha@108')
        cursor = dbConnection.cursor()
        #Create Table
        '''
        delete_table="DROP TABLE ClearedAlarms"
        cursor.execute(delete_table)
        cursor.execute("CREATE TABLE ClearedAlarms (Device VARCHAR(255), InverterName VARCHAR(255), Alarm VARCHAR(255), OccuranceTime VARCHAR(255), Message VARCHAR(255))")
        cursor.execute("SHOW TABLES")
        dbConnection.commit()
        '''

        cursor.executemany("""INSERT INTO ClearedAlarms (Device, InverterName, Alarm, Occurancetime, Message) 
                  VALUES(%(dev_name)s,%(inv_name)s,%(alarm_id)s,%(date_time)s,%(alarm_msg)s)""", logdata)
        dbConnection.commit()
        #print("Row Added into the DB = {}".format(cursor.rowcount))

obj=crowel()
obj.login_req()
obj.elct_generation()
obj.errorlogs()
obj.sqlload_data()
