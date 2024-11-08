import sqlite3

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ Create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def main():
    database = "database_ratings.db"

    sql_create_ratings_table = """CREATE TABLE IF NOT EXISTS ESG_ratings(
                                        ID integer PRIMARY KEY,
                                        Company_name text NOT NULL,
                                        Date_of_rating text,
                                        Score_ESG float,
                                        Nb_articles integer
                                    );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_ratings_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()