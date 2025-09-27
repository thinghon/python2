print("20224016-박소호")

def population(city_n):
    city_f=open("C:\\Users\\박소호\\Documents\\프로그래밍1\\인구.txt",'r', encoding="UTF-8")
    for line in city_f:
        s={}
        (s['cityname'],s['n_people'],s['n_house'],s['p_house'],s['m_population'],s['w_population'],s["mpw"])=line.split(";")
        if city_n == s['cityname']:
            city_f.close()
            return(s)
    city_f.close()
    return({})

running = True
break_1='나가기'
while running:
    city_ff=open("C:\\Users\\박소호\\Documents\\프로그래밍1\\인구.txt",'r', encoding="UTF-8")
    print('도시이름은:')
    n=1
    for line in city_ff:
        (a,b,c,d,e,f,g)=line.split(';')
        print("%s.%s"%(n,a))
        n=n+1
    city_ff.close()
    print('19.나기기')
    search_city = input('검색하고 싶은 도시를  입력하시오:')
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
    
