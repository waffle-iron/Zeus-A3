import config
import mysql.connector

cnx = mysql.connector.connect(user=config.MYSQL_USER, password=config.MYSQL_PASSWORD, host=config.MYSQL_HOST, database=MYSQL_DATABASE)
