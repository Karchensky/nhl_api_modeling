import requests
import json
import pandas as pd
from functions.scraper_endpoint import scraper_endpoint


# This function scrapes the event data for a specific game_id
def scraper_game_events(game_id):
    
    # Establish destination
    endpoint = scraper_endpoint(f'game/{game_id}/feed/live')

    # Send an HTTP GET request to the API endpoint with your query parameter
    response = requests.get(endpoint)

    # Load the JSON data
    data = json.loads(response.text)

    # Extract event data
    events_list = []
    events = data.get("liveData", {}).get("plays", {}).get("allPlays", [])
    for event in events:
        if event['result']['eventTypeId'] in ['SHOT', 'BLOCKED_SHOT', 'MISSED_SHOT', 'GOAL', 'PENALTY']:

        # Game info
        game_id = int(game_id)

        # Event information
        event_id = event.get("about", {}).get("eventIdx")
        event_type = event.get("result", {}).get("eventTypeId")
        event_description = event.get("result", {}).get("description")
        period = event.get("about", {}).get("period")
        period_time = event.get("about", {}).get("periodTime")
        period_remaining_time = event.get("about", {}).get("periodTimeRemaining")
        team_id = event.get("team", {}).get("id")
        x_coord = event.get("coordinates", {}).get("x")
        y_coord = event.get("coordinates", {}).get("y")
        
        # Player information
        if event['event_type'] == 'GOAL':
                    players = event['players']
                    scorer = ''
                    assists = []
                    goalie = ''
                    for player in players:
                        if player['playerType'] == 'Scorer':
                            scorer = player['player']['fullName']
                        elif player['playerType'] == 'Assist':
                            assists.append(player['player']['fullName'])
                        elif player['playerType'] == 'Goalie':
                            goalie = player['player']['fullName']
                    event['scorer'] = scorer
                    event['assist1'] = assists[0] if len(assists) > 0 else ''
                    event['assist2'] = assists[1] if len(assists) > 1 else ''
                    event['goalie'] = goalie

        # Append the play data to the play_data list
        events_list.append([game_id, event_id, event_type, event_description, period, period_time, period_remaining_time, team_id, x_coord, y_coord] + player_ids + player_types)
        
        # Handle goal events and extract additional data
        if event_type == "GOAL":
            secondary_type = event.get("result", {}).get("secondaryType")
            strength = event.get("result", {}).get("strength", {}).get("name")
            events_list[-1] += [secondary_type, strength]

    # Create a pandas dataframe from the play_data list
    headers = [ "GAME_ID","EVENT_ID", "EVENT_TYPE", "EVENT_DESCRIPTION", "PERIOD", "PERIOD_TIME", "PERIOD_REMAINING_TIME", "TEAM_ID", "X_COORD", "Y_COORD",
                "PLAYER1_ID", "PLAYER2_ID", "PLAYER3_ID", "PLAYER4_ID", "PLAYER5_ID", "PLAYER6_ID", "PLAYER1_TYPE", "PLAYER2_TYPE", "PLAYER3_TYPE", "PLAYER4_TYPE", 
                "PLAYER5_TYPE", "PLAYER6_TYPE", "SECONDARY_TYPE", "STRENGTH"]
    df = pd.DataFrame(events_list, columns=headers)

    return df