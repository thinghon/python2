print("20224016-박소호")


print("근의 공식 계산기")
def math(a,b,c):

    D = (b**2) - (4*a*c)
    
    cal1 = (-b + (D**0.5)) / (2*a)
    cal2 = (-b - (D**0.5)) / (2*a)

    if D > 0:
        print(cal1)
        print(cal2)

    elif D == 0:
        print(cal1)

    else:
        print("근이 존재하지 않습니다")

print("이차식이 aX^2 + bX + c일때")
a = int(input("a를 입력하시오:"))
while a == 0:
    print("a는 0이 될수 없습니다.")
    a = int(input("a를 입력하시오:"))
b = int(input("b를 입력하시오:"))
c = int(input("c를 입력하시오:"))
math(a,b,c)
