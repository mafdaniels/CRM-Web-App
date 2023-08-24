
# import mysql.connector
import MySQLdb as Database
import mysql.connector

dataBase = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = 'Mafabi@mysql'

)
 
cursorObject = dataBase.cursor()
 
cursorObject.execute("CREATE DATABASE mafdaniels_database")

print("All Done")
