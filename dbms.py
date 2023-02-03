import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name,user_name,user_password):
	conneect=None
	try:
		connection=mysql.connector.connect(host=host_name,user=user_name,passwd=user_password)
		print('Connect successful')
	except Error as er:
		print(er)
	return connection

pw="Raghav@2104"
db="mysql_python"
connection=create_server_connection("localhost","root",pw)


