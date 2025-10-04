from flask import Flask, render_template
import urllib.request
from bs4 import BeautifulSoup

#기상청 힌남노 태풍 현황 페이지 열기
page = urllib.request.urlopen("https://www.weather.go.kr/w/typhoon/typ-history-pop.do?json=%7B%22typYear%22:2022,%22typSeq%22:11%7D").read()
soup = BeautifulSoup(page,'html.parser') #뷰티풀 수프 객체 생성
#힌남노 태풍 tbody 검색
table = soup.find('tbody', {'id':'testId'})

data = []

#모든 <tr>태그를 검색 각 시간별 데이터를 가져옴
for tr in table.find_all('tr'): #각 시간의 행tr에 대해 반복
    tds = tr.find_all('td') #<td> 검색하여 한 행의 모든 데이터 가져옴
    for td in tds: #하나의 시간 값들 td에 대해 반복
        date = tds[0].text #<td>태그 리스트의 첫번째(인덱스 0)에서 날짜를 가져옴
        date_1 = date.strip() #양쪽 공백을 없앤다
        wind_speed = tds[5].text #<td>태그 리스트의 여섯번째(인덱스 5)에서 풍속(시속)을 가져옴
        wind_speed_1 = wind_speed.strip() #양쪽 공백을 없앤다
        speed = tds[10].text #<td>태그 리스트의 열번째(인덱스 10)에서 이동속도를 가져옴
        speed_1 = speed.strip() #양쪽 공백을 없앤다
        data.append([date_1,wind_speed_1,speed_1]) #data리스트에 날짜,풍속,이동속도를 추가

app = Flask(__name__) #플라스크 객체 생성

@app.route("/")#웹요청 경로 지정
#실행함수 작성
def weather():
    return render_template('weather.html',dv=data)
#플라스크 서버 구동
if __name__=="__main__":
    app.run(host="192.168.0.198", port="8080")#내컴퓨터 ip주소와 포트번호