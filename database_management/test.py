import sqlite3
from add_a_row import add_row

def clear_table():
    connection = sqlite3.connect('database_ratings.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM ESG_ratings;")
    connection.commit()
    connection.close()


add_row("database_ratings.db",('Toto','2024-12-12',1.2,12))
# clear_table()
dates = [f"2024_{k}_01" for k in range(1,12)]
companies = ['Total','Crédit_agricole','Amazon','Shell']

for comp in companies:
    
    for date in dates:
        add_row(comp,date)

conn = sqlite3.connect('database_ratings.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM ESG_ratings")
rows = cursor.fetchall()
print(rows)