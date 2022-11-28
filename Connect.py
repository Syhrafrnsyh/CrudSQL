import mysql.connector
from mysql.connector import Error

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

if db.is_connected():
    print("Bershasil terhubung ke database")
