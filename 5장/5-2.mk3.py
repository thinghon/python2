import urllib.request
from bs4 import BeautifulSoup
page = urllib.request.urlopen("https://fifaonline4.nexon.com/datacenter/rank") #url페이지 읽기
soup = BeautifulSoup(page,'html.parser') #뷰티풀 함수 객체 생성
#데이터 베이스 연결
import sqlite3
conn = sqlite3.connect('fifa4 rank.db')
#연결 객체의 row_factory 속성을 sqlite3.Row클라스로 지정
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

table = soup.find('div',{'class':'tbody'}) #<div class = css-11hjvr8>검색

#모든<tr>태그를 검색 각 랭커의 데이터를 크롤링하고 데이터베이스에 삽입
for div in table.find_all('div',{'class':'tr'}): #각 랭커의 행 tr에 대해 반복
    rank = div.find('span',{'class':'td rank_no'}).text.replace("\n",'')
    name = div.find('span',{'class':'name profile_pointer'}).text.replace("\n",'')
    price = div.find('span',{'class':'price'}).text.replace("\n",'')
    point = div.find('span',{'class':'td rank_r_win_point'}).text.replace("\n",'')
    cursor.execute(''' 
        insert into rank (rank, name, price, point) values(?, ?, ?, ?)''',
        (rank, name, price, point))

#데이터베이스로 내보내기
conn.commit()
cursor.execute("select * from rank") #rank 테이블 모든 데이터 조회 SQL문 실행
rows = cursor.fetchall() #모든행(레코드) 가져오기

#각 행의 열의 값들을 출력
for row in rows: 
    print("랭크: %s, 닉네임: %s, 팀가치: %s, 점수: %s" % (row['rank'], row['name'], row['price'], row['point']))
conn.close() #데이터베이스 연결 종료