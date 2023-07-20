import sqlite3

conn = sqlite3.connect("Ex_App/test.db")

cur = conn.cursor()

names_list = [
    ("Duck", "Dogers"),
    ("Mighty", "Mouse"),
    ("Bart", "Simpson"),
    ("Johnny", "Bravo"),
    ("Sponge", "Bob")
]

cur.executemany("""
        INSERT INTO people (first_name, last_name) VALUES (?, ?)
    """, names_list)

conn.commit()

# cur.execute("""CREATE TABLE IF NOT EXISTS people
#             (first_name TEXT, last_name TEXT)""")
# conn.commit()

cur.close()
conn.close()