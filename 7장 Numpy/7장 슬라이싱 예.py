#20224016-박소호
#슬라이싱 예
import numpy as np

#배열의 정보 출력 함수
def pprint(arr,s):
    print("shape: {}, dimension: {}, dtype: {}". format(arr.shape, arr.ndim, arr.dtype))
    print(s)
    print(arr)

#배열 데이터 생성 후 구조 변경
a1 = np.arange(1,25).reshape((4,6))
pprint(a1, "a1 =>")

#슬라이승 배열 1
s1 = a1[1:3,1:5] #2 X 4배열
pprint(s1,"s1 =>")

s1 = a1[1:-1,1:-1] #2 X 4배열 
pprint(s1,"s1 =>")

#슬라이싱 배열의 슬라이싱
ss1 =s1[:, 1:3]
pprint(ss1, "ss1 =>")

#배열 복사
b1 = np.copy(a1)
pprint(a1,"b1=>")

#슬라이싱을 적용하여 참조한 4개 요소 업데이트 및 슬라이싱 배열 조회
s1[:,1:3] = 99999
pprint(s1,"s1 =>")
pprint(a1,"a1 =>")
pprint(b1,"b1 =>")