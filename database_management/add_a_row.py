import sqlite3
from database_creation import create_connection

def add_row(database, row):
    """
    Create a new project into the projects table
    row is a tuple with the elements to add, without the ID
    row = ('Amazon', '2024-11-08', '43,8', '13')
    """

    conn = create_connection(database)

    

    sql = ''' INSERT INTO ESG_ratings(Company_name,Date_of_rating,Score_ESG,Nb_articles)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, row)
    conn.commit()





def main():
    database = "database_ratings.db"

    row = ('Amazon','2024-11-02',4.3,12)

    add_row(database,row)

if __name__ == '__main__':
    main()
