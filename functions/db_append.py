import sqlite3
from functions.db_set_path import db_set_path

def db_append(table_name, data_frame, db_path = db_set_path()):
    
    # Connect to the database
    conn = sqlite3.connect(db_path)

    # Append our dataframe into our table
    data_frame.to_sql(table_name, conn, schema='main', if_exists='append', index=False)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()