import urllib.request
from bs4 import BeautifulSoup
page = urllib.request.urlopen("https://valorant.op.gg/leaderboards") #url페이지 읽기
soup = BeautifulSoup(page,'html.parser') #뷰티풀 함수 객체 생성
#데이터 베이스 연결
import sqlite3
conn = sqlite3.connect('valo rank.db')
#연결 객체의 row_factory 속성을 sqlite3.Row클라스로 지정
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

table = soup.find('ol',{'class':'css-11hjvr8'}) #<div class = css-11hjvr8>검색

#모든<tr>태그를 검색 각 랭커의 데이터를 크롤링하고 데이터베이스에 삽입
for li in table.find_all('li'): #각 랭커의 행 tr에 대해 반복
    rank = li.find('div',{'class':'rank'}).text.replace("\n",'')
    name = li.find('div',{'class':'player-info'}).text.replace("\n",'')
    tier = li.find('div',{'class':'cell--tier'}).text.replace("\n",'')
    point = li.find('div',{'class':'css-n8rq6u'}).text.replace("\n",'')
    cursor.execute(''' 
        insert into rank (rank, name, tier, point) values(?, ?, ?, ?)''',
        (rank, name, tier, point))

#데이터베이스로 내보내기
conn.commit()
cursor.execute("select * from rank") #rank 테이블 모든 데이터 조회 SQL문 실행
rows = cursor.fetchall() #모든행(레코드) 가져오기
#각 행의 열의 값들을 출력
for row in rows: 
    print("랭크: %s, 닉네임: %s, 티어: %s, 점수: %s" % (row['rank'], row['name'], row['tier'], row['point']))
conn.close() #데이터베이스 연결 종료