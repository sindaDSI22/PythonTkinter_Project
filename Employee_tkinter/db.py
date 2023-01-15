import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Employee (id INTEGER PRIMARY KEY, NomPrenom text, age text, post text, salaire text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM Employee")
        rows = self.cur.fetchall()
        return rows

    def insert(self, NomPrenom, age, post, salaire):
        self.cur.execute("INSERT INTO Employee VALUES (NULL, ?, ?, ?, ?)",
                         (NomPrenom, age, post, salaire))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM Employee WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, NomPrenom, age, post, salaire):
        self.cur.execute("UPDATE Employee SET NomPrenom = ?, age = ?, post = ?, salaire = ? WHERE id = ?",
                         (NomPrenom, age, post, salaire, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



