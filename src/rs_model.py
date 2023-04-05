import sqlite3
import typing
from datetime import datetime

class RunescapeDB:
    conn: sqlite3 = sqlite3.connect('runescape.db')
    tables = [
    '''
    CREATE TABLE IF NOT EXISTS dim_players (
        PID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT UNIQUE
        );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS dim_skills (
        SID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT UNIQUE
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS fact_levels (
        PID INTEGER REFERENCES dim_players(PID),
        SID INTEGER REFERENCES dim_skills(SID),
        Level INTEGER,
        TS Text,
        PRIMARY KEY (PID, SID, TS)
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS fact_rank (
        PID INTEGER REFERENCES dim_players(PID),
        SID INTEGER REFERENCES dim_skills(SID),
        Rank INTEGER,
        TS Text,
        PRIMARY KEY (PID, SID, TS)
        );
    '''
    ]

    #constructor
    def __init__(self) -> None:
        self._init_ddl()

    #destructor
    def __del__(self) -> None:
        self.conn.close()

    def close(self) -> None:
        self.conn.close()

    def _init_ddl(self) -> None:
        for table_ddl in self.tables:
            self.conn.execute(table_ddl)
        self.conn.commit()



    def insert_players(self,players: list[str]) -> int:
        for player in players:
            self.conn.execute("INSERT OR IGNORE INTO dim_players (Name) VALUES (?)", (player,))
        self.conn.commit()
        return 200
        

    def insert_skills(self,skills) -> None:
        for skill in skills:
            self.conn.execute("INSERT OR IGNORE INTO dim_skills (Name) VALUES (?)", (skill,))
        self.conn.commit()

    def insert_levels(self,player_name: str,skill_name: str, level: int) -> None:
        ts: datetime = datetime.now()
        ts_str: str = ts.strftime("%Y/%m/%d")
        insert_sql: str = f'''
        INSERT OR IGNORE INTO fact_levels (PID, SID, Level, TS)
        SELECT p.PID, s.SID, {level}, "{ts_str}"
        FROM dim_players p
        INNER JOIN dim_skills s ON p.Name = "{player_name}" and s.Name = "{skill_name}"
        '''
        self.conn.execute(insert_sql)
        self.conn.commit()

    def insert_ranks(self) -> None:
        pass