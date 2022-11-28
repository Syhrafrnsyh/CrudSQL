import mysql.connector
from mysql.connector import Error
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pysql"
)

#========== INSERT ===================================================================


def insertuser(db):
  nama = input("Masukan nama: ")
  alamat = input("Masukan alamat: ")
  telepon = input("Masukan telepon: ")
  val = (nama, alamat, telepon)
  cursor = db.cursor()
  sql = "INSERT INTO user (nama, alamat, telepon) VALUES (%s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))

def insertsupplier(db):
  kode = input("Masukan kode: ")
  nama = input("Masukan nama: ")
  alamat = input("Masukan alamat: ")
  telepon = input("Masukan telepon: ")
  val = (kode, nama, alamat, telepon)
  cursor = db.cursor()
  sql = "INSERT INTO supplier (kode, nama, alamat, telepon) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))

def insertkategori(db):
  nama = input("Masukan nama: ")
  val = (nama)
  cursor = db.cursor()
  sql = "INSERT INTO kategori (nama) VALUES (%s)"
  cursor.execute(sql,(val,))
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))

def insertbarang(db):
  kode = input("Masukan kode: ")
  nama = input("Masukan nama: ")
  id_kategori = input("Masukan id_kategori: ")
  stok = input("Masukan stok: ")
  harga = input("Masukan harga: ")
  val = (kode, nama, id_kategori, stok, harga)
  cursor = db.cursor()
  sql = "INSERT INTO barang (kode, nama, id_kategori, stok, harga) VALUES (%s, %s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))

#================== SHOW ===========================================================

def show_user(db):
  cursor = db.cursor()
  sql = "SELECT * FROM user"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def show_supplier(db):
  cursor = db.cursor()
  sql = "SELECT * FROM supplier"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def show_kategori(db):
  cursor = db.cursor()
  sql = "SELECT * FROM kategori"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def show_barang(db):
  cursor = db.cursor()
  sql = "SELECT * FROM barang"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

#====================== UPDATE =======================================================

def update_user(db):
  cursor = db.cursor()
  show_user(db)
  id_user = input("pilih id_user> ")
  nama = input("Nama baru: ")
  alamat = input("Alamat baru: ")
  telepon = input("Telepon baru: ")

  sql = "UPDATE user SET nama=%s, alamat=%s, telepon=%s WHERE id_user=%s"
  val = (nama, alamat, telepon, id_user)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))

def update_supplier(db):
  cursor = db.cursor()
  show_supplier(db)
  id_supplier = input("pilih id_supplier> ")
  kode = input("Kode baru: ")
  nama = input("Nama baru: ")
  alamat = input("Alamat baru: ")
  telepon = input("Telepon baru: ")

  sql = "UPDATE supplier SET kode=%s, nama=%s, alamat=%s, telepon=%s WHERE id_supplier=%s"
  val = (kode, nama, alamat, telepon, id_supplier)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))

def update_kategori(db):
  cursor = db.cursor()
  show_kategori(db)
  id_kategori = input("pilih id_kategori> ")
  nama = input("Nama baru: ")

  sql = "UPDATE kategori SET nama=%s WHERE id_kategori=%s"
  val = (nama, id_kategori)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))

def update_barang(db):
  cursor = db.cursor()
  show_barang(db)
  id_barang = input("pilih id_barang> ")
  kode = input("Kode baru: ")
  nama = input("Nama baru: ")
  id_kategori = input("id_kategori baru: ")
  stok = input("Stok baru: ")
  harga = input("Harga baru: ")

  sql = "UPDATE barang SET kode=%s, nama=%s, id_kategori=%s, stok=%s, harga=%s WHERE id_barang=%s"
  val = (kode, nama, id_kategori, stok, harga, id_barang)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))

#===================== DELETE ========================================================

def delete_user(db):
  cursor = db.cursor()
  show_user(db)
  id_user = input("pilih id_user> ")
  sql = "DELETE FROM user WHERE id_user=%s"
  val = (id_user,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))

def delete_supplier(db):
  cursor = db.cursor()
  show_supplier(db)
  id_supplier = input("pilih id_supplier> ")
  sql = "DELETE FROM supplier WHERE id_supplier=%s"
  val = (id_supplier,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))

def delete_kategori(db):
  cursor = db.cursor()
  show_kategori(db)
  id_kategori = input("pilih id_kategori> ")
  sql = "DELETE FROM kategori WHERE id_kategori=%s"
  val = (id_kategori,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def delete_barang(db):
  cursor = db.cursor()
  show_barang(db)
  id_barang = input("pilih id_barang> ")
  sql = "DELETE FROM barang WHERE id_barang=%s"
  val = (id_barang,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))

#===================== SEARCH ========================================================

def search_user(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM user WHERE nama LIKE %s OR telepon LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def search_supplier(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM supplier WHERE nama LIKE %s OR telepon LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def search_kategori(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM kategori WHERE nama LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def search_barang(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM barang WHERE nama LIKE %s OR kode LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)
      
#==================MENU INSERT===========================================================

def insert_menu(db):
  print("==============")
  print("    INSERT    ")
  print("==============")
  print("1. Insert User")
  print("2. Insert Supplier")
  print("3. Insert Kategori")
  print("4. Insert Barang")
  print("0. Keluar")
  print("------------------")
  menuinsert = input("Pilih menu> ")

  #clear screen
  os.system("clear")

    #clear screen
  os.system("clear")

  if menuinsert == "1":
    insertuser(db)
  elif menuinsert == "2":
    insertsupplier(db)
  elif menuinsert == "3":
    insertkategori(db)
  elif menuinsert == "4":
    insertbarang(db)
  elif menuinsert == "0":
    exit()
  else:
    print("Menu salah!")
    
#==================== MENU SHOW ========================================================

def menu_show(db):
  print("==============")
  print("    SHOW    ")
  print("==============")
  print("1. Show User")
  print("2. Show Supplier")
  print("3. Show Kategori")
  print("4. Show Barang")
  print("0. Keluar")
  print("------------------")
  menushow = input("Pilih menu> ")

  #clear screen
  os.system("clear")

    #clear screen
  os.system("clear")

  if menushow == "1":
    show_user(db)
  elif menushow == "2":
    show_supplier(db)
  elif menushow == "3":
    show_kategori(db)
  elif menushow == "4":
    show_barang(db)
  elif menushow == "0":
    exit()
  else:
    print("Menu salah!")
#================================ MENU UPDATE =============================================

def update_menu(db):
  print("==============")
  print("    UPDATE    ")
  print("==============")
  print("1. Update User")
  print("2. Update Supplier")
  print("3. Update Kategori")
  print("4. Update Barang")
  print("0. Keluar")
  print("------------------")
  menuupdate = input("Pilih menu> ")

  #clear screen
  os.system("clear")

    #clear screen
  os.system("clear")

  if menuupdate == "1":
    update_user(db)
  elif menuupdate == "2":
    update_supplier(db)
  elif menuupdate == "3":
    update_kategori(db)
  elif menuupdate == "4":
    update_barang(db)
  elif menushow == "0":
    exit()
  else:
    print("Menu salah!")

#============================== MENU DELETE ===============================================

def delete_menu(db):
  print("==============")
  print("    DELETE    ")
  print("==============")
  print("1. Delete User")
  print("2. Delete Supplier")
  print("3. Delete Kategori")
  print("4. Delete Barang")
  print("0. Keluar")
  print("------------------")
  menudelete = input("Pilih menu> ")

  #clear screen
  os.system("clear")

    #clear screen
  os.system("clear")

  if menudelete == "1":
    delete_user(db)
  elif menudelete == "2":
    delete_supplier(db)
  elif menudelete == "3":
    delete_kategori(db)
  elif menudelete == "4":
    delete_barang(db)
  elif menushow == "0":
    exit()
  else:
    print("Menu salah!")
#============================ MENU SEARCH =================================================

def search_menu(db):
  print("==============")
  print("    SEARCH    ")
  print("==============")
  print("1. Search User")
  print("2. Search Supplier")
  print("3. Search Kategori")
  print("4. Search Barang")
  print("0. Keluar")
  print("------------------")
  menusearch = input("Pilih menu> ")

  #clear screen
  os.system("clear")

    #clear screen
  os.system("clear")

  if menusearch == "1":
    search_user(db)
  elif menusearch == "2":
    search_supplier(db)
  elif menusearch == "3":
    search_kategori(db)
  elif menusearch == "4":
    search_barang(db)
  elif menushow == "0":
    exit()
  else:
    print("Menu salah!")

#===================== MENU UTAMA ========================================================

def show_menu(db):
  print("=== MENU UTAMA ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_menu(db)
  elif menu == "2":
    menu_show(db)
  elif menu == "3":
    update_menu(db)
  elif menu == "4":
    delete_menu(db)
  elif menu == "5":
    search_menu(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)
