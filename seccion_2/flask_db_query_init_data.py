import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

names = [('Federico', 36), ('Mateo', 20), ('Tomas', 18), ('Pedro', 45), ('Juan', 60)]

for name, age in names:
    print(name, age)
    cur.execute("INSERT INTO users (user_name, user_age) VALUES (?, ?)",
            (name, age)
            )

connection.commit()
connection.close()
