import sqlite3
from functions.db_set_path import db_set_path

# This function appends records to our database. It is often used in conjuction with the db_list_fresh_game_ids function & a particular scraper.
def db_append(table_name, data_frame):
    
    # Connect to the database
    conn = sqlite3.connect(db_set_path())

    # Append our dataframe into our table
    data_frame.to_sql(table_name, conn, schema='main', if_exists='append', index=False)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()