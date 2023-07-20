# import sqlite3

# conn = sqlite3.connect("Ex_App/members.db")
# cur = conn.cursor()

# with open("Ex_App/test.sql") as file:
#     sql_script = file.read()

# cur.executescript(sql_script)

# cur.close()
# conn.close()

##############################

import sqlite3

conn = sqlite3.connect("Ex_App/members.db")
cur = conn.cursor()

member_data = cur.execute("SELECT * FROM members ORDER BY ln")
for row in member_data:
    print(row)

cur.close()
conn.close()

