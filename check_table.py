import sqlite3 as sl

def check_students_table() -> None:
    con = sl.connect('entrance.db')
    with con:
        data = con.execute("select count(*) from sqlite_master where type='table' and name='students'")
        for row in data:
            if row[0] == 0:
                with con:
                    con.execute("""
                        CREATE TABLE students (
                        ID INT PRIMARY KEY,
                        DIRECTION1 NVARCHAR(511),
                        DIRECTION2 NVARCHAR(511),
                        DIRECTION3 NVARCHAR(511),
                        DIRECTION4 NVARCHAR(511),
                        DIRECTION5 NVARCHAR(511),
                        SCORE INT NOT NULL,
                        GAVE BOOL,
                        WHERE NVARCHAR(255),
                        );
                                """)
    
def check_direction_tables(direct_name) -> None:
    con = sl.connect('entrance.db')
    with con: 
        data = con.execute(f"select count(*) from sqlite_master where type='table' and name='{direct_name}'")
        for row in data:
            if row[0] == 0:
                with con:
                    con.execute(
                        f"CREATE TABLE {direct_name} (" +
                        """
                        ID INT PRIMARY KEY,
                        PLACE INT NOT NULL,
                        SCORE INT NOT NULL,
                        ATESTAT_HERE BOOL,
                        OWN_PROGRESS INT,
                        );
                        """)
                    
		
def check_college_tables(college_name) -> None:
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
                        DIR_NAME NVARCHAR(511),
                        Q_PLACE INT
                        );
                        """)