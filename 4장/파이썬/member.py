import sqlite3
import datetime

conn = sqlite3.connect("member.db")
cursor = conn.cursor()

id1 = 'wynam'
pwd1 = 'n1234'
name1 = '남윤영'
time1 = datetime.datetime.now()
cursor

cursor.execute("""insert into meminfo (id, password, name, time)values(?,?,?,?)""",(id1,pwd1,name1,time1))
print("첫번째 사용자 레코드 추가 성공")
id2 = 'jklee'
pwd2 = 'l3456'
name2 = '이전경'
time2 = datetime.datetime.now()
cursor.execute("""insert into meminfo (id, password, name, time)values(?,?,?,?)""",(id2,pwd2,name2,time2))
print("두번째 사용자 레코드 추가 성공")

conn.commit()
conn.close()