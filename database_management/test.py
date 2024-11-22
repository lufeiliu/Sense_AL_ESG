import sqlite3
from add_a_row import add_row
import random
def clear_table():
    connection = sqlite3.connect('database_ratings.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM ESG_ratings;")
    connection.commit()
    connection.close()


clear_table()
dates = [f"2024-{k}-01" for k in range(1,12)]
companies = ['Total','Crédit_agricole','Amazon','Shell']

for comp in companies:
    pic = random.randint(1,11)
    time = random.randint(1,2)
    print("pic=",pic)
    print("time=",time)
    for k,date in enumerate(dates):
        score = random.random()/3
        if k==pic:
            score*=2.5
        if k+1==pic and time ==2:
            score*=2.5
        add_row(comp,date,score,5)

conn = sqlite3.connect('database_ratings.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM ESG_ratings")
rows = cursor.fetchall()
print(rows)