#20224016-박소호
#배열 생성 예
#Numpy 임포드트
import numpy as np
#1차원 배열
arr1 = np.array([1 ,2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr1) #배열 출력
print(arr1[3]) #4
print(arr1[3 : 6]) #4, 5, 6
print(arr1.shape) #배열 차원의 크기 : (10,)
print(arr1.dtype) #배열 요소의 자료형: int32

#2차원 배열, 2 x 3배열
arr2 = np.array([[1.0, 2.0, 3.0],[4.4, 5.5, 6.6]])
print(arr2)  #배열 출력
print(arr2[1]) #[4.4, 5.5, 6.6]
print(arr2[1,2]) #6.6
print(arr2[1][2]) #6.6
print(arr2.shape) #(2,3)
print(arr2.dtype) #float64
print(arr2.ndim) #차원(축)의 개수 : 2
print(arr2.size) #원소의 개수 : 6

#3차언 배열, 2 X 3 X 4 배열
arr3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[11,12,13,14],[15,16,17,18],[19,20,21,22]]])
print(arr3)
print(arr3[0])
print(arr3[1,2])
print(arr3[1,2,0])
print(arr3[1][2][0])
print(arr3.shape)
print(arr3.dtype)
print(arr3.ndim)
print(arr3.size)