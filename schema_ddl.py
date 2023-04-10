from functions.db_write import db_write

sql_statement = db_write(''' 

DROP TABLE IF EXISTS PLAYER_GAME_LOGS

''')

sql_statement = db_write(''' 

CREATE TABLE IF NOT EXISTS PLAYER_GAME_LOGS (
    GAME_ID                     INTEGER         PRIMARY_KEY,
    PLAYER_ID                   INTEGER         PRIMARY_KEY,
    TEAM_ID                     INTEGER,
    PLAYER_NAME                 TEXT,
    BIRTHDATE                   DATE,
    CURRENTAGE                  INTEGER,
    POSITION                    TEXT,
    TIME_ON_ICE                 TEXT,
    ASSISTS                     INTEGER,         
    GOALS                       INTEGER,
    SHOTS                       INTEGER,
    HITS                        INTEGER,
    POWER_PLAY_GOALS            INTEGER,
    POWER_PLAY_ASSISTS          INTEGER,
    PENALTY_MINUTES             INTEGER,
    SHORT_HANDED_GOALS          INTEGER,
    SHORT_HANDED_ASSISTS        INTEGER,
    BLOCKED                     INTEGER,
    PLUS_MINUS                  INTEGER,
    EVEN_TIME_ON_ICE            TEXT,
    POWER_PLAY_TIME_ON_ICE      TEXT,
    SHORT_HANDED_TIME_ON_ICE    TEXT
)

''')

sql_statement = db_write(''' 

DROP TABLE IF EXISTS TEAM_SCHEDULE

''')

sql_statement = db_write(''' 

CREATE TABLE IF NOT EXISTS TEAM_SCHEDULE (
    GAME_ID                 INTEGER         PRIMARY_KEY,
    HOME_TEAM_ID            INTEGER,
    AWAY_TEAM_ID            INTEGER,
    SEASON                  TEXT,
    GAME_DATE               DATE,
    GAME_STATE              TEXT,
    HOME_TEAM_NAME          TEXT,
    AWAY_TEAM_NAME          TEXT,
    HOME_SCORE              INTEGER,
    AWAY_SCORE              INTEGER,
    HOME_TEAM_WINS          INTEGER,
    HOME_TEAM_LOSSES        INTEGER,
    HOME_TEAM_OT_LOSSES     INTEGER,
    AWAY_TEAM_WINS          INTEGER,
    AWAY_TEAM_LOSSES        INTEGER,
    AWAY_TEAM_OT_LOSSES     INTEGER
)

''')