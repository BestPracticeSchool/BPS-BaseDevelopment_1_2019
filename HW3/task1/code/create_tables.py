import sqlite3 

conn = sqlite3.connect('data.db')
cur = conn.cursor()

query_create = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
cur.execute(query_create)

query_create = "CREATE TABLE IF NOT EXISTS items (name TEXT, price TEXT)"
cur.execute(query_create)

conn.commit()
conn.close()
