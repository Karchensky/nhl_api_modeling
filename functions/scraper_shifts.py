import requests
import json
import pandas as pd
from functions.scraper_endpoint import scraper_endpoint
from functions.time_text_to_seconds import time_text_to_seconds

# This function scrapes the shift data when given a specific game_id
def scraper_shifts(game_id):
    
    # Establish destination
    endpoint = scraper_endpoint(f'{game_id}', api_shift_alternate=True)

    # Send an HTTP GET request to the API endpoint with your query parameter
    response = requests.get(endpoint)

    # Load the JSON data
    data = json.loads(response.text)

    # Extract shift data
    shift_data = []

    for shift in data['data']:
        shift_id = shift['id']
        game_id = shift['gameId']
        team_id = shift['teamId']
        player_id = shift['playerId']
        shift_number = shift['shiftNumber']
        period = shift['period']
        start_time = shift['startTime']
        end_time = shift['endTime']
        duration = shift['duration']
        start_time_in_seconds = time_text_to_seconds(start_time)
        end_time_in_seconds= time_text_to_seconds(end_time)
        duration_in_seconds = time_text_to_seconds(duration)

        # Append each shift
        shift_data.append([ shift_id, game_id, team_id, player_id, shift_number, period, start_time, end_time, duration, start_time_in_seconds, end_time_in_seconds, duration_in_seconds ])

    # Convert shift data to a Pandas DataFrame and print as table
    headers = [ "SHIFT_ID", "GAME_ID", "TEAM_ID", "PLAYER_ID", "SHIFT_NUMBER", "PERIOD", "START_TIME", "END_TIME", "DURATION", "START_TIME_IN_SECONDS", "END_TIME_IN_SECONDS", "DURATION_IN_SECONDS"]
               
    df = pd.DataFrame(shift_data, columns=headers)

    return df