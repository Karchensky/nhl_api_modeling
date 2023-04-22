import requests
import json
import pandas as pd
import sqlite3
from functions.db_set_path import db_set_path
from functions.scraper_endpoint import scraper_endpoint

# This function scrapes the rosters to get a distinct list of players and player id's
def scraper_players(season):

    # Establish destination
    endpoint = scraper_endpoint(f'teams?expand=team.roster&season={season}')

    # Send an HTTP GET request to the API endpoint with your query parameter
    response = requests.get(endpoint)

    # Load the JSON data
    data = json.loads(response.text)

    # Connect to the database
    conn = sqlite3.connect(db_set_path())

    # Initialize an empty list to store the player data
    players = []
    # Loop through each team in the data
    for team in data["teams"]:
        # Loop through each player in the team's roster
        for player in team["roster"]["roster"]:
            # Extract the player's ID and full name
            player_id = player["person"]["id"]
            player_name = player["person"]["fullName"]

            # Check if the player already exists in the database
            query = f"SELECT COUNT(*) FROM STG_PLAYERS WHERE PLAYER_ID = {player_id}"
            player_count = conn.execute(query).fetchone()[0]

            if player_count == 0:

                # Append the player data to the list
                players.append([ player_id, player_name ])

    # Convert season to a Pandas DataFrame and print as table
    headers = [ "PLAYER_ID", "PLAYER_NAME"]

    df = pd.DataFrame(players, columns=headers)

    # Drop any duplicate rows
    df.drop_duplicates(inplace=True)

    return df