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