import sqlite3
from functions.db_set_path import db_set_path

# This function executes a SQL statement against our database.
def db_write(sql_statement):
    
    # Connect to the database
    conn = sqlite3.connect(db_set_path())

    # Create a cursor object
    cur = conn.cursor()

    # What is the SQL statement we want to execute
    sql_statement = sql_statement

    # Execute the create tables statements
    cur.execute(sql_statement)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()