#20224016-박소호
#배열 연산 - 집계 함수 예2
import numpy as np

#배열의 정보 출력 함수
def pprint(arr,s):
    print("shape: {}, dimension: {}, dtype: {}". format(arr.shape, arr.ndim, arr.dtype))
    print("Array`s Data:\n", arr)
    print(s)
    print(arr)

a = np.array([[1,2,3],[4,5,6],[7,8,9]]) #오퍼랜드 a
pprint(a,"a`s data =>")

b = np.array([[9,8,7],[6,5,4],[3,2,1]]) #오퍼랜드 b
pprint(b, "b`s data=>")

#전체 성분의 최소값, 최대값이 위치한 인덱스를 반환(argmin, argmax)
agx = a.argmax()
pprint(agx, "agx = a.argmax()=>")

agn = a.argmin()
pprint(agn,"agn = a.argmin()=>")

agx0 = a.argmax(axis=0)
pprint(agx0,"agx0 = a.argmax(axis=0)=>")

agn1 = a.argmin(axis=1)
pprint(agn1, "agn1 = a.argmin(axis=1)=>")

#맨 처음 성분부터 각 성분까지의 누적합 또는 누적곱을 계산(cumsum, cumprod)
cs = a.cumsum()
pprint(cs,"cs = a.cumsum()=>")

cs1 = a.cumsum(axis=1)
pprint(cs1, "cs1 = a.cumsum(axis=1)=>")