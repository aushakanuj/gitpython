import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "CREATE TABLE users (id INT AUTO_INCREMENT, username VARCHAR(20) , password VARCHAR(50),PRIMARY KEY (id))"

cursor.execute(create_table)

user = (1, "jose", "1102")

inser_query = "INSERT INTO users VALUES(?,?,?)"

cursor.execute(inser_query, user)

users = [(2, "bob", "1234"), (3, "rol", "qweasdzxc")]
cursor.executemany(inser_query, users)


select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
