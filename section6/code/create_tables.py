import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" #important to use the whole word INTEGER instead of int to create increamenting numbers
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)" #important to use the whole word INTEGER instead of int to create increamenting numbers
cursor.execute(create_table)


connection.commit()

connection.close()