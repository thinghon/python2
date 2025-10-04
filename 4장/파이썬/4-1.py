print("20224016-박소호")
import sqlite3

conn = sqlite3.connect('member.db')

conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute('select*from meminfo')
rows = cursor.fetchall()

for row in rows:
    print("ID: %s, password: %s, name: %s, time: %s" %(row['id'],row['password'],row['name'],row['time']))
cursor.close()