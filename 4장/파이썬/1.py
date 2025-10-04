import urllib.request
from bs4 import BeautifulSoup
page = urllib.request.urlopen("https://sports.news.naver.com/wfootball/record/index?category=epl&tab=team&year=2021")
soup = BeautifulSoup(page,'html.parser')

import sqlite3
conn = sqlite3.connect('EPL team rank.db')

conn.row_factory = sqlite3.Row
cursor = conn.cursor()

table = soup.find('div',{'id':"wfootballTeamRecordBody"})
data = []

for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    for td in tds:
        rank = tds[0].text.replace("\n",'')
        name_team = tds[1].text.replace("\n",'')
        match = tds [13].text.replace("\n",'')
        goal = tds[2].text.replace("\n",'')  

        ra = rank.strip()
        na = name_team.strip()
        ma = match.strip()
        go = goal.strip()    
        data.append([ra,na,ma,go])

conn.commit()
print(data)

rows = cursor.fetchall()

for row in rows:
    print("\n순위: %s, 이름_팀:%s, 경기수: %s, 득점수:%s" %
                (row['ra'],row['na'],row['ma'],row['go']))
conn.close()