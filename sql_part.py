import sqlite3 as sl

def check_students_table() -> None:
    con = sl.connect('entrance.db')
    with con:
        data = con.execute("select count(*) from sqlite_master where type='table' and name='students'")
        for row in data:
            if row[0] == 0:
                with con:
                    con.execute("""
                        CREATE TABLE IF NOT EXISTS Students 
                        (
                        id INT PRIMARY KEY,
                        direction1 VARCHAR(511),
                        direction2 VARCHAR(511),
                        direction3 VARCHAR(511),
                        direction4 VARCHAR(511),
                        direction5 VARCHAR(511),
                        score INT NOT NULL,
                        gave BOOL,
                        place VARCHAR(255)
                        )
                                """)
    con.commit()
    con.close()
    
def check_direction_tables(direct_name:str) -> None:
    con = sl.connect('entrance.db')
    with con: 
        data = con.execute(f"select count(*) from sqlite_master where type='table' and name='{direct_name}'")
        for row in data:
            if row[0] == 0:
                with con:
                    con.execute(f"""CREATE TABLE IF NOT EXISTS {direct_name} (
                    place INT NOT NULL,
                    id VARCHAR(127),
                    way VARCHAR(127),
                    score INT NOT NULL,
                    own_progress INT,
                    atestat_here BOOL,
                    prioritery INT
                    )
                    """)
    con.commit()
    con.close()
                    
		
def check_college_tables(college_name:str) -> None:
    con = sl.connect('entrance.db')
    with con: 
        data = con.execute(f"select count(*) from sqlite_master where type='table' and name='{college_name}'")
        for row in data:
            if row[0] == 0:
                with con:
                    con.execute(
                        f"CREATE TABLE {college_name} (" +
                        """
                        ID INT PRIMARY KEY,
                        DIR_NAME VARCHAR(511),
                        Q_PLACE INT
                        );
                        """)
    con.commit()
    con.close()

def add_to_direction_tables(direction_name:str, place:int, Id:str, way:str, points:int, 
                          own_achives:int, certificate:bool, prioritery:int) -> None:
    con = sl.connect('entrance.db')
    curs = con.cursor()
    curs.execute(f'INSERT INTO {direction_name} (place, id, way, score, own_progress, atestat_here, prioritery) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                    (place, Id, way, points, own_achives, certificate, prioritery))
    con.commit()
    con.close()
