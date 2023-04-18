from functions.scraper_game_events import scraper_game_events
from functions.db_list_fresh_game_ids import db_list_fresh_game_ids
from functions.db_append import db_append

scrape = scraper_game_events('2022010001')
distinct_events = scrape['EVENT_TYPE'].unique()

print(distinct_events)
print(scrape)



# Scrape all the game logs that we don't already have recorded in our table
# for game_id in db_list_fresh_game_ids("STG_GAME_EVENTS"):
#     db_append('STG_GAME_EVENTS', scraper_game_events(game_id))