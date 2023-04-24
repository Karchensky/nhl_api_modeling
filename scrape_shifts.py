from functions.scraper_shifts import scraper_shifts
from functions.db_list_fresh_game_ids import db_list_fresh_game_ids
from functions.db_append import db_append

## Scrape all the shifts that we don't already have recorded in our table
for game_id in db_list_fresh_game_ids("STG_SHIFTS"):
    db_append('STG_SHIFTS', scraper_shifts(game_id))