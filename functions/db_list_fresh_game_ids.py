import sqlite3
import pandas as pd
from functions.db_set_path import db_set_path

# This function identifies new game IDs for ingestion into our database. We use this for incremental loading of tables & to ensure no duplicates are loaded.
def db_list_fresh_game_ids(table_name):

    # Connect to the database
    conn = sqlite3.connect(db_set_path())

    # Query for all game IDs that are in FINAL state
    game_ids_query = "SELECT GAME_ID FROM STG_SCHEDULE WHERE GAME_STATE = 'Final'"
    game_ids_df = pd.read_sql(game_ids_query, conn)

    # Query for all game IDs that already exist in the target table
    target_table_query = f"SELECT DISTINCT GAME_ID FROM {table_name}"
    target_table_df = pd.read_sql(target_table_query, conn)

    # Filter out any game IDs that already exist in the target table
    unprocessed_game_ids = game_ids_df[~game_ids_df["GAME_ID"].isin(target_table_df["GAME_ID"])]

    # Convert filtered game IDs to a list
    fresh_game_id_list = unprocessed_game_ids["GAME_ID"].tolist()

    # Close the connection
    conn.close()

    return fresh_game_id_list