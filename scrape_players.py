import datetime
from functions.scraper_players import scraper_players
from functions.db_append import db_append

# Scrape all the rosters starting in 2018 --> the current year
start_season = 2018
end_season = datetime.datetime.now().year

# loop through seasons
for season in range(start_season, end_season):

    # format season for API request
    season_str = str(season) + str(season+1)

    # Append players to table
    db_append('STG_PLAYERS', scraper_players(season_str))