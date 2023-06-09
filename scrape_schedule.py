import datetime
from functions.scraper_schedule import scraper_schedule
from functions.db_append import db_append

# Scrape all the games starting in 2018 --> the current year
start_season = 2018
end_season = datetime.datetime.now().year

# loop through seasons
for season in range(start_season, end_season):

    # format season for API request
    season_str = str(season) + str(season+1)

    # Append season to table
    db_append('STG_SCHEDULE', scraper_schedule(season_str))