import sqlite3


connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTs users (id INTEGER PRIMARY KEY, username text , password text)"

create = "CREATE TABLE IF NOT EXISTs items (name text, price int)"


cursor.execute(create_table)
cursor.execute(create)


connection.commit()

connection.close()
