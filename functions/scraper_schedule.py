import requests
import json
import pandas as pd
from datetime import datetime
from functions.scraper_endpoint import scraper_endpoint

# This function scrapes the schedule
def scraper_schedule(season):

    # Establish destination
    endpoint = scraper_endpoint(f'schedule')

    # Set season parameter as season
    params = {"season": season}

    # Send an HTTP GET request to the API endpoint with your query parameter
    response = requests.get(endpoint, params=params)

    # Load the JSON data
    data = json.loads(response.text)

    # Extract schedule for the season
    schedule = []
    for date in data['dates']:
        for game in date['games']:
            game_id = int(game['gamePk'])
            game_type = game['gameType']
            season = game['season']
            game_date = datetime.strptime(game['gameDate'], '%Y-%m-%dT%H:%M:%SZ').date()
            game_state = game['status']['detailedState']
            home_team_id = game['teams']['home']['team']['id']
            away_team_id = game['teams']['away']['team']['id']
            home_team_name = game['teams']['home']['team']['name']
            away_team_name = game['teams']['away']['team']['name']
            home_score = game['teams']['home']['score']
            away_score = game['teams']['away']['score']
            home_team_wins = game['teams']['home']['leagueRecord']['wins']
            home_team_losses = game['teams']['home']['leagueRecord']['losses']
            home_team_ot_losses = game['teams']['home']['leagueRecord'].get('ot', 0)
            away_team_wins = game['teams']['away']['leagueRecord']['wins']
            away_team_losses = game['teams']['away']['leagueRecord']['losses']
            away_team_ot_losses = game['teams']['away']['leagueRecord'].get('ot', 0)

            # Append each game record to our season
            schedule.append([   game_id, game_type, season, game_date, game_state, home_team_id, away_team_id, home_team_name, away_team_name, home_score, away_score,
                                home_team_wins, home_team_losses, home_team_ot_losses, away_team_wins, away_team_losses, away_team_ot_losses ])

    # Convert season to a Pandas DataFrame and print as table
    headers = [ "GAME_ID", "GAME_TYPE", "SEASON", "GAME_DATE", "GAME_STATE", "HOME_TEAM_ID", "AWAY_TEAM_ID", "HOME_TEAM_NAME", "AWAY_TEAM_NAME", "HOME_SCORE", "AWAY_SCORE", 
                "HOME_TEAM_WINS","HOME_TEAM_LOSSES","HOME_TEAM_OT_LOSSES","AWAY_TEAM_WINS","AWAY_TEAM_LOSSES","AWAY_TEAM_OT_LOSSES"]
    df = pd.DataFrame(schedule, columns=headers)
    df = df[(df["GAME_TYPE"] != "PR")]

    return df