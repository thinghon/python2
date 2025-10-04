#20224016-박소호
# 배열 초기화 생성 예
import numpy as np

#배열의 정보 출력 함수
def pprint(arr):
    print("shape: {}, dimension: {}, dtype: {}". format(arr.shape, arr.ndim, arr.dtype))
    print("Array`s Data:\n", arr)

a = np.zeros((3,4))
pprint(a)

a = np.ones((2,3,4), dtype = np.int16)
pprint(a)

a = np.full((2,2),7)
pprint(a)

a = np.empty((4, 2))
pprint(a)

a = np.array([[1,2,3],[4,5,6]])
b = np.ones_like(a)
pprint(b)