import urllib.request
from bs4 import BeautifulSoup

print("20224016-박소호")

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

print(data) #리스트 data 출력

with open('hinnamno.csv','w',encoding='utf8')as file:  #hinnamno.csv파일을 쓰기 모드로 열기
    file.write('힌남노 태풍 날짜,풍속(시속),이동속도\n') #컬럼 이름 추가
    for i in data: #리스트의 각 항목에 대해
            file.write('{0},{1},{2}\n'.format(i[0],i[1],i[2])) #도시, 온도, 습도를 줄 단위로 저장