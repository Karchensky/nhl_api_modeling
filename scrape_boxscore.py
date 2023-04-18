from functions.scraper_boxscore import scraper_boxscore
from functions.db_list_fresh_game_ids import db_list_fresh_game_ids
from functions.db_append import db_append

# Scrape all the game logs that we don't already have recorded in our table
for game_id in db_list_fresh_game_ids("STG_BOXSCORE"):
    db_append('STG_BOXSCORE', scraper_boxscore(game_id))