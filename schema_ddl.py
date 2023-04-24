from functions.db_write import db_write

# This table will house the raw schedule
sql_statement = db_write('''DROP TABLE IF EXISTS STG_SCHEDULE''')
sql_statement = db_write('''CREATE TABLE IF NOT EXISTS STG_SCHEDULE (
    GAME_ID                 INTEGER         PRIMARY_KEY,
    GAME_TYPE               TEXT,
    SEASON                  TEXT,
    GAME_DATE               DATE,
    GAME_STATE              TEXT,
    HOME_TEAM_ID            INTEGER,
    AWAY_TEAM_ID            INTEGER,
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

# This table will house the raw team list & their corresponding ID's
sql_statement = db_write('''DROP TABLE IF EXISTS STG_TEAMS''')
sql_statement = db_write('''CREATE TABLE IF NOT EXISTS STG_TEAMS (
    TEAM_ID                 INTEGER         PRIMARY_KEY,
    TEAM_NAME               TEXT,
    TEAM_ABBREVIATION       TEXT
)
''')

# This table will house the raw player list
sql_statement = db_write('''DROP TABLE IF EXISTS STG_PLAYERS''')
sql_statement = db_write('''CREATE TABLE IF NOT EXISTS STG_PLAYERS (
    PLAYER_ID               INTEGER         PRIMARY_KEY,
    PLAYER_NAME             TEXT
)
''')

# This table will house the raw boxscore data
sql_statement = db_write('''DROP TABLE IF EXISTS STG_BOXSCORE''')
sql_statement = db_write('''CREATE TABLE IF NOT EXISTS STG_BOXSCORE (
    GAME_ID                             INTEGER         PRIMARY_KEY,
    PLAYER_ID                           INTEGER         PRIMARY_KEY,
    TEAM_ID                             INTEGER,
    POSITION                            TEXT,
    TIME_ON_ICE                         TEXT,
    ASSISTS                             INTEGER,         
    GOALS                               INTEGER,
    SHOTS                               INTEGER,
    HITS                                INTEGER,
    POWER_PLAY_GOALS                    INTEGER,
    POWER_PLAY_ASSISTS                  INTEGER,
    PENALTY_MINUTES                     INTEGER,
    SHORT_HANDED_GOALS                  INTEGER,
    SHORT_HANDED_ASSISTS                INTEGER,
    BLOCKED                             INTEGER,
    PLUS_MINUS                          INTEGER,
    EVEN_TIME_ON_ICE                    TEXT,
    POWER_PLAY_TIME_ON_ICE              TEXT,
    SHORT_HANDED_TIME_ON_ICE            TEXT,
    EVEN_TIME_ON_ICE_IN_SECONDS         INTEGER,
    POWER_PLAY_TIME_ON_ICE_IN_SECONDS   INTEGER,
    SHORT_HANDED_TIME_ON_ICE_IN_SECONDS INTEGER
)
''')

# This table will house the raw game event data
sql_statement = db_write('''DROP TABLE IF EXISTS STG_GAME_EVENTS''')
sql_statement = db_write('''CREATE TABLE IF NOT EXISTS STG_GAME_EVENTS (
    GAME_ID                     INTEGER         PRIMARY_KEY,
    EVENT_ID                    TEXT            PRIMARY_KEY,
    EVENT_TYPE                  TEXT,
    EVENT_DESCRIPTION           TEXT,
    PERIOD                      INTEGER,
    PERIOD_TIME                 TEXT,
    PERIOD_TIME_IN_SECONDS      INTEGER,
    TEAM_ID                     INTEGER,
    X_COORD                     INTEGER,
    Y_COORD                     INTEGER,
    PLAYER_ID                   INTEGER,
    SHOOTER_ID                  INTEGER,
    SCORER_ID                   INTEGER,
    PRIMARY_ASSIST_ID           INTEGER,
    SECONDARY_ASSIST_ID         INTEGER,
    GOALIE_ID                   INTEGER,
    GOAL_TYPE                   TEXT,
    GOAL_STRENGTH               TEXT,
    GOAL_EMPTY_NET_IND          BOOLEAN
)
''')

# This table will house the raw shift data
sql_statement = db_write('''DROP TABLE IF EXISTS STG_SHIFTS''')
sql_statement = db_write('''CREATE TABLE IF NOT EXISTS STG_SHIFTS (
    SHIFT_ID                INTEGER         PRIMARY_KEY,
    GAME_ID                 INTEGER,
    TEAM_ID                 INTEGER,
    PLAYER_ID               INTEGER,
    SHIFT_NUMBER            INTEGER,
    PERIOD                  INTEGER,
    START_TIME              TEXT,
    END_TIME                TEXT,
    DURATION                TEXT,
    START_TIME_IN_SECONDS   INTEGER,
    END_TIME_IN_SECONDS     INTEGER,
    DURATION_IN_SECONDS     INTEGER
)
''')