#20224016-박소호
#배열 연산 - 집계 함수 예1
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

#sum() 집계 함수
s_none = a.sum()
pprint(s_none,"s_none = a.sum() =>")

s_0 = a.sum(axis=0)
pprint(s_0,"s_0 = a.sum(axis=0) =>")

s_1 = a.sum(axis=1)
pprint(s_1,"s_1 = a.sum(axis=1) =>")

#max() 집계 함수
mx_none = a.max()
pprint(mx_none,"mx_none = a.max()=>")

mx_0 = a.max(axis=0)
pprint(mx_0,"mx_0 = a.max(axis=0)=>")

mx_1 = a.max(axis=1)
pprint(mx_1,"mx_1 = a.max(axis=1)=>")

#mean() 집계 함수
mn_none = a.mean()
pprint(mn_none, "mn_none = a.mean()=>")

mn_0 = a.mean(axis=0)
pprint(mn_0,"mn_0 = a.mean(axis=0)")

mn_1 = a.mean(axis=1)
pprint(mn_1,"mn_1 = a.mean(axis=1)=>")