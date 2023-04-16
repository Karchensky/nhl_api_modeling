from functions.scraper_player_game_logs_boxscore import scraper_player_game_logs_boxscore
from functions.db_list_fresh_game_ids import db_list_fresh_game_ids
from functions.db_append import db_append

# Scrape all the game logs that we don't already have recorded in our table
for game_id in db_list_fresh_game_ids("PLAYER_GAME_LOGS_BOXSCORE"):
    db_append('PLAYER_GAME_LOGS_BOXSCORE', scraper_player_game_logs_boxscore(game_id))