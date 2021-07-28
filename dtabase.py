import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="")

cursor = db.cursor()
cursor.execute("CREATE DATABASE nama_pelanggan")




db = mysql.connector.connect(host="localhost", user="root", passwd="", database="nama_pelanggan")

mycursor = db.cursor()
sql = """CREATE TABLE pelanggan(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)

)
"""
mycursor.execute(sql)

