from functions.scraper_power_play_toi import scraper_power_play_toi
from functions.db_list_fresh_game_ids import db_list_fresh_game_ids
from functions.db_append import db_append

# Scrape all the game logs that we don't already have recorded in our table
for game_id in db_list_fresh_game_ids("STG_POWER_PLAY_TOI"):
    db_append('STG_POWER_PLAY_TOI', scraper_power_play_toi(game_id))