import sqlite3

# Connect to the database
conn = sqlite3.connect('electronics_store.db')
cursor = conn.cursor()

# List all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:", tables)

conn.close()
