print("20224016-박소호")
from population import*
from cityfind import*

city_n=0
population(city_n)

running = True
break_1='나가기'
while running:
    search_city=cityfind()
    city=population(search_city)
    if search_city == break_1:
        break;
    else:
        if city:
            print("행정기관:     "+city['cityname'])
            print("총인구수:     "+city['n_people'])
            print("세대수:       "+city['n_house'])
            print("세대당 인구:  "+city['p_house'])
            print("남자 인구수:  "+city['m_population'])
            print("여자 인구수:  "+city['w_population'])
            print("남여비율:     "+city['mpw'])