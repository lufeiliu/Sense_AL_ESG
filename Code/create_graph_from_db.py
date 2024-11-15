import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime


def create_graph_from_name(Company_name):
    conn = sqlite3.connect('database_ratings.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ESG_ratings WHERE Company_name= ?", (Company_name,))
    rows = cursor.fetchall()

    dates = []
    ratings = []
    for row in rows:
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        ratings.append(row[3])

    plt.figure(figsize=(10, 5))
    plt.plot(dates, ratings, marker='o', linestyle='-', color='b')
    plt.title(f'ESG rating of {Company_name}')
    plt.xlabel('Date')
    plt.ylabel('ESG score')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()




create_graph_from_name('Amazon')