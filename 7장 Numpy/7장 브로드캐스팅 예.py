#20224016-박소호
#브로드캐스팅 예
import numpy as np

#배열의 정보 출력 함수
def pprint(arr,s):
    print("shape: {}, dimension: {}, dtype: {}". format(arr.shape, arr.ndim, arr.dtype))
    print(s)
    print(arr)

a = np.array([[0,0,0],[10,10,10],[20,20,20],[30,30,30]]) #오퍼랜드 a, 4 X 3
pprint(a,"a =>")

b = np.array([[0,1,2],[0,1,2],[0,1,2],[0,1,2]]) #오퍼랜드 b, 4 X 3
pprint(b, "b =>")

#같은 구조 배열 덧셈
c = a + b
pprint(c,"c =>")

#b1 브로드캐스팅
b1 = np.array([[0,1,2]])
pprint(b1, "b1 =>")

c1 = a + b1
pprint(c1, "c1 =>")

#a1 브로드캐스팅
a1 = np.array([[0],[10],[20],[30]])
pprint(a1, "a1 =>")

c2 = a1 + b;
pprint(c1, "c2 =>")