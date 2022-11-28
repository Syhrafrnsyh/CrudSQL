import mysql.connector
from mysql.connector import Error

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE pysql")

print("Database berhasil dibuat!")
