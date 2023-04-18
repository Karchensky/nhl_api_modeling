from functions.scraper_teams import scraper_teams
from functions.db_append import db_append

# Scrape the team list with ID, full name, and abbreviations
db_append('STG_TEAMS', scraper_teams())