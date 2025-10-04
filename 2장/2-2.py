print("20224016-박소호")

import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen("http://www.weather.go.kr/weather/observation/currentweather.jsp").read()
soup = BeautifulSoup(page,'html.parser') 

table = soup.find('table', {'id':'weather_table'})
found_time = soup.find(class_ = 'cmp-table-topinfo')

data = []

for tr in table.find_all('tr'): 
    tds = tr.find_all('td') 
    for td in tds: 
        if td.find('a'): 
           point = td.find('a').text 
           temperature = tds[5].text 
           humidity = tds[9].text 
           data.append([found_time.text[5:], point, temperature, humidity])            

print(found_time.text[5:])
print(data)

with open('weather_mk1.csv', 'w', encoding = 'utf8')as file:
    file.write('Time, point, temperature, humidity\n') 
    for i in data: 
        file.write('{0},{1},{2},{3}\n'.format(i[0],i[1],i[2],i[3])) 