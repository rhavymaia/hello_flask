import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO pessoas (nome, email) VALUES (?, ?)",
            ('João da Silva', 'jsilva@mail.com')
            )

connection.commit()
connection.close()
