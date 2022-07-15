import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
#print(a[1:9]) # 이상 미만
print(a[3:]) # 이상 
print(a[:3]) # 미만 
print(a[-3:-1]) # 이상 미만 
print(a[1:8:3]) # 이상 미만 스텝
print(a[::2]) # 모든 스텝 

b = np.array([[1,2,3,4],[5,6,7,8]])
print(b[1, 1:3]) # 1번째배열의 1이상 3미만
print(b[0:2, 2]) # 모든 배열의 2인덱스컬럼 
print(b[0:2, 1:3]) # 모든 배열의 1이상 3미만 컬럼 

 