import sqlite3
from database_creation import create_connection

def add_row(companie,date,score,nb_articles):
    """
    Create a new project into the projects table
    row is a tuple with the elements to add, without the ID
    row = ('Amazon', '2024-11-08', '43,8', '13')
    """

    row = (companie,date,score,nb_articles)

    conn = create_connection("database_ratings.db")
    

    sql = ''' INSERT INTO ESG_ratings(Company_name,Date_of_rating,Score_ESG,Nb_articles)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, row)
    conn.commit()





def main():
    pass

if __name__ == '__main__':
    main()
