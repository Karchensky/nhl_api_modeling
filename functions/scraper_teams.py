import requests
import pandas as pd
from functions.scraper_endpoint import scraper_endpoint

# This function scrapes the box scores for player data when given a specific game_id
def scraper_teams():
    
    # Establish destination
    endpoint = scraper_endpoint(f'teams')

    # Send an HTTP GET request to the API endpoint with your query parameter
    response = requests.get(endpoint)

    # Load the JSON data
    data = response.json()

    teams = []
    for team in data['teams']:
        team_id = team['id']
        team_name = team['name']
        team_abbreviation = team['abbreviation']

        # Append each game record to our team list
        teams.append((team_id, team_name, team_abbreviation))

        # Convert season to a Pandas DataFrame and print as table
        headers = [ "TEAM_ID", "TEAM_NAME", "TEAM_ABBREVIATION"]
        df = pd.DataFrame(teams, columns=headers)

    return df