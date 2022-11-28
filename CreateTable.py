import mysql.connector
from mysql.connector import Error

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pysql"
)

cursor = db.cursor()

A1 = """CREATE TABLE user (
  id_user int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nama varchar(100)  NOT NULL,
  alamat varchar(100)  NOT NULL,
  telepon varchar(20)  NOT NULL
)
"""

A2 = """CREATE TABLE supplier (
  id_supplier int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  kode varchar(10)  NOT NULL,
  nama varchar(100)  NOT NULL,
  alamat varchar(100)  NOT NULL,
  telepon varchar(20)  NOT NULL
)
"""

A3 = """CREATE TABLE kategori (
  id_kategori int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nama varchar(100) NOT NULL
)
"""

A4 = """CREATE TABLE barang (
  id_barang int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  kode varchar(10)  NOT NULL,
  nama varchar(100) NOT NULL,
  id_kategori int(11) NOT NULL,
  stok int(11) NOT NULL,
  harga double(10,2) NOT NULL,
  CONSTRAINT FOREIGN KEY (id_kategori) REFERENCES kategori (id_kategori) ON DELETE CASCADE ON UPDATE CASCADE
)
"""



cursor.execute(A1)
cursor.execute(A2)
cursor.execute(A3)
cursor.execute(A4)

cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

#print("Tabel berhasil dibuat!")
