from functions.scraper_penalty_kill_toi import scraper_penalty_kill_toi
from functions.db_list_fresh_game_ids import db_list_fresh_game_ids
from functions.db_append import db_append

# Scrape all the game logs that we don't already have recorded in our table
for game_id in db_list_fresh_game_ids("STG_PENALTY_KILL_TOI"):
    db_append('STG_PENALTY_KILL_TOI', scraper_penalty_kill_toi(game_id))