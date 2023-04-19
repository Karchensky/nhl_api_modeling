# nhl_api_modeling

----

* Repo designed to:

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

* Notes to use this repo:

    1) packages: sqlite3, pandas, json, requests, datetime
    2) set your datbase path/location to a local destination the db_set_path function
    3) run the schema_ddl.py file to create the database
    4) not set up yet: there will likely be 2 files you can choose to execute... first time run vs. incremental / daily run for when we get this thing going and we just want to update our daily stats, as opposed to rerunning the entire database.  For now, you can run the "scrape_" programs after running the schema_ddl to populate tables one at a time - in order of dependencies, just make sure to execute the schedule first. 
    5) ...
    6) profit

---

* Other Notes:

    1) Additional steps/notes will be added as this gets more fleshed out.
    2) The goal is for this to be ready for the 2023/2024 season... will be working on it occasionally when I get time outside of work.
    3) Does anyone know if there is a clean way to see onIce player_id's per each event? I don't see it in the API. Also - is there a good way to get game log data for team stats (outside of just the normal goals/assists/etc.)? Specifically looking for stuff like shot attempts for/against, time at 5on5, 5on4, etc - not just # of penalties. I can back into some of these things with the player events & box scores.. but directly off the API would certainly be easier. 

---