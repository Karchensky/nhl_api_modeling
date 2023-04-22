import requests
import json
import pandas as pd
from functions.scraper_endpoint import scraper_endpoint
from functions.time_text_to_seconds import time_text_to_seconds

# This function scrapes the box scores for player data when given a specific game_id
def scraper_boxscore(game_id):
    
    # Establish destination
    endpoint = scraper_endpoint(f'game/{game_id}/boxscore')

    # Send an HTTP GET request to the API endpoint with your query parameter
    response = requests.get(endpoint)

    # Load the JSON data
    data = json.loads(response.text)

    # Extract player stats
    player_stats = []
    for team in ["away", "home"]:
        team_id = int(data["teams"][team]["team"]["id"])
        for player_id, player_data in data["teams"][team]["players"].items():

            # Make sure the record is legit
            if player_data.get("person", {}).get("fullName"):

                # Game info
                game_id = int(game_id)

                # Skater bio
                player_id = int(player_data["person"]["id"])
                if "primaryPosition" in player_data["person"]:
                    position = player_data["person"]["primaryPosition"]["abbreviation"]
                else:
                    position = "N/A"
                    
                # Skater stats
                if "skaterStats" in player_data["stats"]:
                    stats = player_data.get("stats", {}).get("skaterStats", {})
                    time_on_ice = stats.get("timeOnIce")
                    assists = stats.get("assists")
                    goals = stats.get("goals")
                    shots = stats.get("shots")
                    hits = stats.get("hits")
                    power_play_goals = stats.get("powerPlayGoals")
                    power_play_assists = stats.get("powerPlayAssists")
                    penalty_minutes = stats.get("penaltyMinutes")
                    short_handed_goals = stats.get("shortHandedGoals")
                    short_handed_assists = stats.get("shortHandedAssists")
                    blocked = stats.get("blocked")
                    plus_minus = stats.get("plusMinus")
                    even_time_on_ice = stats.get("evenTimeOnIce")
                    power_play_time_on_ice = stats.get("powerPlayTimeOnIce")
                    short_handed_time_on_ice = stats.get("shortHandedTimeOnIce")
                    even_time_on_ice_in_seconds =  time_text_to_seconds(even_time_on_ice)
                    power_play_time_on_ice_in_seconds = time_text_to_seconds(power_play_time_on_ice)
                    short_handed_time_on_ice_in_seconds = time_text_to_seconds(short_handed_time_on_ice)
                else:
                    time_on_ice = 0
                    assists = 0
                    goals = 0
                    shots = 0
                    hits = 0
                    power_play_goals = 0
                    power_play_assists = 0
                    penalty_minutes = 0
                    short_handed_goals = 0
                    short_handed_assists = 0
                    blocked = 0
                    plus_minus = 0
                    even_time_on_ice = 0
                    power_play_time_on_ice = 0
                    short_handed_time_on_ice = 0
                    even_time_on_ice_in_seconds = 0
                    power_play_time_on_ice_in_seconds = 0
                    short_handed_time_on_ice_in_seconds = 0

                # Append each player to player stats
                player_stats.append([   game_id, player_id, team_id, position, time_on_ice, assists, goals, shots, hits, 
                                        power_play_goals, power_play_assists, penalty_minutes, short_handed_goals, short_handed_assists, 
                                        blocked, plus_minus, even_time_on_ice, power_play_time_on_ice, short_handed_time_on_ice, 
                                        even_time_on_ice_in_seconds, power_play_time_on_ice_in_seconds, short_handed_time_on_ice_in_seconds])

    # Convert player stats to a Pandas DataFrame and print as table
    headers = [ "GAME_ID", "PLAYER_ID", "TEAM_ID", "POSITION", "TIME_ON_ICE", "ASSISTS", "GOALS", "SHOTS", "HITS",
                "POWER_PLAY_GOALS", "POWER_PLAY_ASSISTS", "PENALTY_MINUTES", "SHORT_HANDED_GOALS", "SHORT_HANDED_ASSISTS",
                "BLOCKED", "PLUS_MINUS", "EVEN_TIME_ON_ICE", "POWER_PLAY_TIME_ON_ICE", "SHORT_HANDED_TIME_ON_ICE",
                "EVEN_TIME_ON_ICE_IN_SECONDS", "POWER_PLAY_TIME_ON_ICE_IN_SECONDS", "SHORT_HANDED_TIME_ON_ICE_IN_SECONDS"]
    df = pd.DataFrame(player_stats, columns=headers)
    df = df[(df["TIME_ON_ICE"] != "0:00") & (df["TIME_ON_ICE"] != 0)]

    return df