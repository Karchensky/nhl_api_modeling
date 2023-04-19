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

# Extract event data
    events_list = []
    events = data.get("liveData", {}).get("plays", {}).get("allPlays", [])
    for event in events:
        event_type = event.get("result", {}).get("eventTypeId")
        if event_type in ['SHOT', 'BLOCKED_SHOT', 'MISSED_SHOT', 'GOAL', 'PENALTY']:
            
            # Game info
            game_id = int(game_id)

            # Event information
            event_id = event.get("about", {}).get("eventIdx")
            event_description = event.get("result", {}).get("description")
            period = event.get("about", {}).get("period")
            period_time = event.get("about", {}).get("periodTime")
            period_remaining_time = event.get("about", {}).get("periodTimeRemaining")
            team_id = event.get("team", {}).get("id")
            x_coord = event.get("coordinates", {}).get("x")
            y_coord = event.get("coordinates", {}).get("y")

            # Extract player details - will vary a bit by event type
            players_involved = event.get("players", [])
            if event_type == "GOAL":
                # player_name = players_involved[0].get("player", {}).get("fullName") if len(players_involved) >= 1 else None
                player_id = int(players_involved[0].get("player", {}).get("id")) if len(players_involved) >= 1 else 0
                shooter_id = player_id
                scorer_id = player_id
                primary_assist_id = int(players_involved[1].get("player", {}).get("id")) if len(players_involved) >= 3 else None
                secondary_assist_id = int(players_involved[2].get("player", {}).get("id")) if len(players_involved) >= 4 else None
                goalie_id = int(players_involved[-1].get("player", {}).get("id")) if len(players_involved) >= 2 else None
                goal_type = event.get("result", {}).get("secondaryType")
                goal_strength = event.get("result", {}).get("strength", {}).get("name")
                goal_empty_net_ind = event.get("result", {}).get("emptyNet")
            if event_type in ['SHOT', 'MISSED_SHOT']:
                # player_name = players_involved[0].get("player", {}).get("fullName") if len(players_involved) >= 1 else None
                player_id = int(players_involved[0].get("player", {}).get("id")) if len(players_involved) >= 1 else None
                shooter_id = player_id
                scorer_id = None
                primary_assist_id = None
                secondary_assist_id = None
                goalie_id = int(players_involved[-1].get("player", {}).get("id")) if len(players_involved) >= 1 else None
                goal_type = None
                goal_strength = None
                goal_empty_net_ind = None
            if event_type in ['BLOCKED_SHOT']:
                # player_name = players_involved[-1].get("player", {}).get("fullName") if len(players_involved) >= 1 else None
                player_id = int(players_involved[-1].get("player", {}).get("id")) if len(players_involved) >= 1 else None
                shooter_id = player_id
                scorer_id = None
                primary_assist_id = None
                secondary_assist_id = None
                goalie_id = None
                goal_type = None
                goal_strength = None
                goal_empty_net_ind = None
            if event_type in ['PENALTY']:
                # player_name = players_involved[0].get("player", {}).get("fullName") if len(players_involved) >= 1 else None    
                player_id = int(players_involved[0].get("player", {}).get("id")) if len(players_involved) >= 1 else None
                shooter_id = None
                scorer_id = None
                primary_assist_id = None
                secondary_assist_id = None
                goalie_id = None
                goal_type = None
                goal_strength = None
                goal_empty_net_ind = None

            # Append the play data to the play_data list
            events_list.append([game_id, event_id, event_type, event_description, period, period_time, period_remaining_time, team_id, x_coord, y_coord, player_id,  shooter_id, scorer_id, primary_assist_id, secondary_assist_id, goalie_id, goal_type, goal_strength, goal_empty_net_ind])

    # Create a pandas dataframe from the play_data list
    headers = [ "GAME_ID","EVENT_ID", "EVENT_TYPE", "EVENT_DESCRIPTION", "PERIOD", "PERIOD_TIME", "PERIOD_REMAINING_TIME", "TEAM_ID", "X_COORD", "Y_COORD",
                "PLAYER_ID", "SHOOTER_ID", "SCORER_ID", "PRIMARY_ASSIST_ID", "SECONDARY_ASSIST_ID", "GOALIE_ID", "GOAL_TYPE", "GOAL_STRENGTH", "GOAL_EMPTY_NET_IND"]
    df = pd.DataFrame(events_list, columns=headers)

    return df