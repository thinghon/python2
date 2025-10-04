#20224016-박소호
#계단 오르내리기 예제 - 파이썬
import random

position = 0
walk = [] #계단 위치 리스트
steps = 100
for i in range(steps): #100회 반복
    if random.randint(0,1): # 0<= n <=1 인 난수 발생, 1이면 참
        step = 1 #계단 오르기
    else:
        step = -1 #계단 내리기

    position += step #계단 위치 값 갱신
    walk.append(position) #리스트에 추가

import matplotlib.pyplot as plt

x = range(steps)  #x축 : 0~99(100회 반복)
plt.title("Random walk with +1/-1 steps")
plt.plot(x,walk)
plt.show()