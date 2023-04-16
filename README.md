# nhl_api_modeling

Repo designed to:

1) access & scrape NHL API: https://statsapi.web.nhl.com/api/v1
    - all scraper functions are titled "scraper_" - and are designed to scrape specific resources from the API (schedule, game logs, teams, etc.)
    - these functions get called by the "scrape_" py files which also insert scraped records into our local database.
2) construct a local database to store scraped NHL API data
    - all db functions are titled "db_" - and are designed to help construct / maintain our database (set path/create, append, write to, etc.)
    - these functions are used in the "scrape_" py files as well - where we scrape & then insert the output into our local database.
    - there will be additional .sql files created that create custom tables for modeling purposes where we will add transformations to our raw scraped data.
3) build predictive models off NHL data to be used for betting purposes
    - TBD: will start once our database is contructed & populated with necessary data.
4) establish an update process so odds can be computed daily with all relevant up-to-date data
    - TBD: will come after our database is constructed & we figure out what we want to model (likely first off the bat: % chance X player to score a goal in a given game)


----
To use this repo:
1) install required packages: sqlite3, pandas, json, requests, datetime
2) pick a database path/location via the db_set_path function
3) run the schema_ddl.py file to create the database
4) run scrape_schedule (game_id's from the schedule are used for incremental loading / identification of new records in other tables).
5) ...
6) profit
---

Other Notes:

    1) Additional steps/notes will be added as this gets more fleshed out.
    2) The goal is for this to be ready for the 2023/2024 season... will be working on it occasionally when I get time outside of work.