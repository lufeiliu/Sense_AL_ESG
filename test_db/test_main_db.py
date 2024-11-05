import sqlite3
from database import create_connection

def add_project(conn, project):
    """
    Create a new project into the projects table
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def main():
    database = "pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)

    with conn:
        # create a new project
        project = ('Cool Project', '2024-11-05', '2025-11-05')
        project_id = add_project(conn, project)
        print(f"Project added with ID: {project_id}")

if __name__ == '__main__':
    main()
