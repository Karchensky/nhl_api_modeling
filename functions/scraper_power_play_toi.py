import requests
import json
import pandas as pd
from functions.scraper_endpoint import scraper_endpoint

# This function scrapes the power play time on ice team statistics in a given game
def scraper_power_play_toi(game_id):
    
    # Establish destination
    endpoint = scraper_endpoint(f'{game_id}', power_play_toi_alternate=True)

    # Send an HTTP GET request to the API endpoint with your query parameter
    response = requests.get(endpoint)

    # Load the JSON data
    data = json.loads(response.text)

    # Extract TOI data
    power_play_toi_data = []

    for toi in data['data']:
        game_id = int(game_id)
        team_id = int(toi['teamId'])
        season = int(toi['seasonId'])
        pp_toi_5_on_4 = int(toi['timeOnIce5v4'])
        pp_toi_5_on_3 = int(toi['timeOnIce5v3'])
        pp_toi_4_on_3 = int(toi['timeOnIce4v3'])
        pp_toi_total = int(toi['timeOnIcePp'])
        ppOpportunities = int(toi['ppOpportunities'])
        goals_for_5v4 = int(toi['goals5v4'])
        goals_for_5v3 = int(toi['goals5v3'])
        goals_for_4v3 = int(toi['goals4v3'])

        # Append each game
        power_play_toi_data.append([ game_id, team_id, season, pp_toi_5_on_4, pp_toi_5_on_3, pp_toi_4_on_3, pp_toi_total, ppOpportunities, goals_for_5v4, goals_for_5v3, goals_for_4v3])

    # Convert power play time on ice data to a Pandas DataFrame and print as table
    headers = [ "GAME_ID", "TEAM_ID", "SEASON", "PP_TOI_5_ON_4", "PP_TOI_5_ON_3", "PP_TOI_4_ON_3", "PP_TOI_TOTAL", "PPOPPORTUNITIES", "GOALS_FOR_5V4", "GOALS_FOR_5V3", "GOALS_FOR_4V3"]
               
    df = pd.DataFrame(power_play_toi_data, columns=headers)

    return df