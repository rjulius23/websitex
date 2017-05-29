#!flask/bin/python3.4
from app import app
import sqlite3

conn = sqlite3.connect('users.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, password TEXT, type TEXT)')
print ("Table created successfully")
conn.close()

host = "127.0.0.1"
port = 5000
debug = True

app.run(host, port, debug) #options can be added

