def cityfind():
    city_ff=open("C:\\Users\\박소호\\Documents\\프로그래밍1\\인구.txt",'r', encoding="UTF-8")
    print('도시이름은:')
    n=1
    for line in city_ff:
        (a,b,c,d,e,f,g)=line.split(';')
        print("%s.%s"%(n,a))
        n=n+1
    city_ff.close()
    print('19.나기기')
    return(input('검색하고 싶은 도시를  입력하시오:'))