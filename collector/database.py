import pymysql.cursors

class Database:
    connection = None

    def __init__(self):
        print("Initializing Database...")

    def connect_db(self):
        if self.connection is not None:
            return self.connection
        else:
            # Reconnect to DB
            self.connection = pymysql.connect(host='localhost',
                                        user='admin',
                                        password='KoralTayeb1102',
                                        database='air_sensor_iot',
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor)
            return self.connection