import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS vehicle(
            id Integer Primary Key,
            Name text,
            Type text,
            No_Passengers text,
            AC text,
            Size text,
            Load text
        )
        """
        self.cur.execute(sql)
        self.con.commit()
        

    # Insert Function
    def insert(self, Name, Type, No_Passengers, AC, Size, Load):
        self.cur.execute("INSERT INTO vehicle VALUES (NULL,?,?,?,?,?,?)",
                         (Name, Type, No_Passengers, AC, Size, Load))
        self.con.commit()
       

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from vehicle")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from vehicle where id=?", (id,))
        self.con.commit()
        

o = Database("cab_service.db")