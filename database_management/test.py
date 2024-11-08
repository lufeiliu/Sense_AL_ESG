import sqlite3

conn = sqlite3.connect('database_ratings.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM ESG_ratings")
rows = cursor.fetchall()
print(rows)