import requests
import json
import pandas as pd
from functions.scraper_endpoint import scraper_endpoint

# This function scrapes the power penalty kill ice team statistics in a given game
def scraper_penalty_kill_toi(game_id):
    
    # Establish destination
    endpoint = scraper_endpoint(f'{game_id}', penalty_kill_toi_alternate=True)

    # Send an HTTP GET request to the API endpoint with your query parameter
    response = requests.get(endpoint)

    # Load the JSON data
    data = json.loads(response.text)

    # Extract TOI data
    penalty_kill_toi_data = []

    for toi in data['data']:
        game_id = int(game_id)
        team_id = int(toi['teamId'])
        season = int(toi['seasonId'])
        pk_toi_4_on_5 = int(toi['timesShorthanded4v5'])
        pk_toi_3_on_5 = int(toi['timesShorthanded3v5'])
        pk_toi_3_on_4 = int(toi['timesShorthanded3v4'])
        pk_toi_total = int(toi['timeOnIceShorthanded'])
        timesShorthanded = int(toi['timesShorthanded'])
        goals_against_4_on_5 = int(toi['goalsAgainst4v5'])
        goals_against_3_on_5 = int(toi['goalsAgainst3v5'])
        goals_against_3_on_4 = int(toi['goalsAgainst3v4'])

        # Append each game
        penalty_kill_toi_data.append([ game_id, team_id, season, pk_toi_4_on_5, pk_toi_3_on_5, pk_toi_3_on_4, pk_toi_total, timesShorthanded, goals_against_4_on_5, goals_against_3_on_5, goals_against_3_on_4])

    # Convert power play time on ice data to a Pandas DataFrame and print as table
    headers = [ "GAME_ID", "TEAM_ID", "SEASON", "PK_TOI_4_ON_5", "PK_TOI_3_ON_5", "PK_TOI_3_ON_4", "PK_TOI_TOTAL", "TIMESSHORTHANDED", "GOALS_AGAINST_4_ON_5", "GOALS_AGAINST_3_ON_5", "GOALS_AGAINST_3_ON_4" ]
               
    df = pd.DataFrame(penalty_kill_toi_data, columns=headers)

    return df