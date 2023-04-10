import datetime
from functions.scraper_player_game_logs import scraper_player_game_logs
from functions.db_append import db_append

# We are going to scrape all the games from 2018-2019 season onward. 
start_season = 2018
end_season = datetime.datetime.now().year

for season in range(start_season, end_season):
    if season in [2018, 2019, 2020]:
        num_teams = 31
    elif season >= 2021:
        num_teams = 32
        
        for game_num in range(1, (num_teams*82/2) + 1):
            game_id = str(season) + '02' + str(game_num).zfill(4)
            db_append('PLAYER_GAME_LOGS', scraper_player_game_logs(game_id))
