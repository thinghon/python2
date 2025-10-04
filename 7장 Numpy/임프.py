#20224016-박소호
import urllib.request
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

page = urllib.request.urlopen("https://weather.naver.com/") #url페이지 읽기
soup = BeautifulSoup(page,'html.parser') #뷰티풀 함수 객체 생성

table = soup.find('ul',{'week_list'}) 

a=1
low_data = np.array([])
high_data = np.array([])

for lis in table.find_all('li'):
    div = lis.find('div',{'cell_temperature'})
    for divs in div.find_all('strong'):
        low_temp = divs.find('span',{'lowest'}).text.replace("\n",'')
        low_temp = low_temp[4:5]
        high_temp = divs.find('span',{'highest'}).text.replace("\n",'')
        high_temp = high_temp[4:6]
        low_data = np.append(low_data, np.array([int(low_temp)]))
        high_data = np.append(high_data, np.array([int(high_temp)]))



x = range(len(high_data))

y = range(len(low_data))

plt.plot(x,high_data, label = 'high temp')
plt.plot(y,low_data, label = 'low temp')
plt.title("weekly template")
plt.xlabel("date")
plt.legend()
plt.show()