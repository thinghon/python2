#20224016-박소호
import urllib.request 
from bs4 import BeautifulSoup
page = urllib.request.urlopen("http://www.weather.go.kr/weather/observation/currentweather.jsp").read()
soup = BeautifulSoup(page, 'html.parser')

import sqlite3 
conn = sqlite3.connect('City Weather.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

table_time = soup.find('div', { 'class': 'cmp-table-topinfo' })
current_time = table_time.text[5:]

dt = current_time.split('.') 
year = dt[0]
month = dt[1] 
date = dt[2]
time = dt[3] 
date_time = year +"-" + month + "-" + date + " " + time
print(date_time)
table = soup.find('table', { 'id': 'weather_table' })
data = []
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    for td in tds:
        if td.find('a'):
            city = td.find('a').text
            temperature = tds[5].text
            humidity = tds[9].text
            data.append([city, temperature, humidity])
            cursor.execute(''' 
            insert into CityWeather (city, temperature, humidity, dtime) values(?, ?, ?, ?)''',
                (city, temperature, humidity, date_time))
conn.commit()

cursor.execute('select * from CityWeather where temperature > 20')
rows = cursor.fetchall()
for row in rows: 
    print("도시: %s, 온도: %s, 습도: %s, 시간: %s" % (row['city'], row['temperature'], row['humidity'], row['dtime']))
conn.close()