import sqlite3 as sq
from users import u

# with sq.connect('saper.db') as con:
#      cur = con.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS users (
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         sex INTEGER NOT NULL DEFAULT 1,
#         old INTEGER,
#         score INTEGER
#     )""")

# cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?)" , (3, 'Маша', 1, 24, 300))
# con.commit()

# con.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?)", u)
# con.commit()

with sq.connect('saper.db') as con:
     cur = con.cursor()
     
cur.execute("SELECT * FROM users WHERE old > 20 AND score > 2000 AND sex == 1")
result = cur.fetchall()
print(result)