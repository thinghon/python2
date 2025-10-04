#20224016-박소호
#계단 오르내리기 예제 - NumPy

import numpy as np

def pprint(arr, s):
    print("shape: {}, dimension: {}, dtype: {}". format(arr.shape, arr.ndim, arr.dtype))
    print(s)
    print(arr)

nsteps = 100

#각 계단 위치의 난수 배열, 0<= n <2
draws = np.random.randint(0,2,size=nsteps)
pprint(draws,"draws =>")

#각 계단오르기/내리기 배열
steps = np.where(draws>0,1,-1)
pprint(steps, "steps = >")

#계단의 위치 값(누적 합)배열
walk = steps.cumsum()
pprint(walk,"walk =>")

import matplotlib.pyplot as plt

x = range(nsteps)
plt.title("Random wlak with +1/-1 steps")
plt.plot(x,walk)
plt.show()