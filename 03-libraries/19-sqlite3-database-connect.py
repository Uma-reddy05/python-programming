"""
Day 19 - sqlite3 database connect
Author - Uma
Date - 23-10-2026
"""


import sqlite3

# Connect to database (creates it if missing)
connection = sqlite3.connect("students.db")

# Create a cursor
cursor = connection.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

print("Database and table created!")

connection.commit()
connection.close()
