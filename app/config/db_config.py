import mysql.connector


#BASES DE DATOS EN LA NUBE
#def get_db_connection():
 ##   return mysql.connector.connect(
   ##     host="b4doekmqoqseuuhpvht5-mysql.services.clever-cloud.com",
     ##   user="uue9rqthiufqqio1",
       ## password="x82mk1uF5pwGK3vCsd5z",
      ##  database="b4doekmqoqseuuhpvht5"
    ##)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mascotas"
    )