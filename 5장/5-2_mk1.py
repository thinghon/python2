import urllib.request
from bs4 import BeautifulSoup
page = urllib.request.urlopen("https://www.op.gg/leaderboards/tier?region=kr") #url페이지 읽기
soup = BeautifulSoup(page,'html.parser') #뷰티풀 함수 객체 생성
#데이터 베이스 연결
import sqlite3
conn = sqlite3.connect('lol rank.db')
#연결 객체의 row_factory 속성을 sqlite3.Row클라스로 지정
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

table = soup.find('div',{'class':'css-ndvmk6 e1fnyy5m0'}) #<div class = css-ndvmk6 e1fnyy5m0>검색

a=1
#모든<tr>태그를 검색 각 랭커의 데이터를 크롤링하고 데이터베이스에 삽입
for tr in table.find_all('tr'): #각 랭커의 행 tr에 대해 반복
    tds = tr.find_all('td') #모든 <td>태그를 검색해 한 랭커의 데이터 리스트 생성
    for td in tds: #한랭커의 데이터를  td에 대해 반복
            a += 1
            rank = tds[0].text.replace("\n",'') #<td>태그 첫번째에서 랭크 등수를 가져옴
            name = tds[1].text.replace("\n",'') #<td>태그 두번째에서 랭커 닉네임를 가져옴
            tier = tds[2].text.replace("\n",'') #<td>태그 세번째에서 티어를 가져옴
            point = tds[3].text.replace("\n",'') #<td>태그 네번째에서 점수를 가져옴
            if(a%7==0): #각 랭커들의 데이터가 7번씩 반복해서 나타나 7번 반복 할때마다 한번만 데이터를 저장한다
                #레코드 삽입 SQL문 실행
                cursor.execute(''' 
                    insert into rank (rank, name, tier, point) values(?, ?, ?, ?)''',
                    (rank, name, tier, point)) # 테이블 rank에 각각의 행에 변수들을 넣는다

#데이터베이스로 내보내기
conn.commit()
cursor.execute("select * from rank") #rank 테이블 모든 데이터 조회 SQL문 실행
rows = cursor.fetchall() #모든행(레코드) 가져오기
#각 행의 열의 값들을 출력
for row in rows: 
    print("랭크: %s, 닉네임: %s, 티어: %s, 점수: %s" % (row['rank'], row['name'], row['tier'], row['point']))
conn.close() #데이터베이스 연결 종료