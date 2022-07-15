import numpy as np

a = np.array([1,2,3,4,5])
a2 = a.copy() #새로운 복사배열이 생성됨
a3 = a.view() #기본 배열을 참조함
a[0] = 10
print(a)
print(a2)
print(a3)
print()

print(a2.base) #None
print(a3.base) #a를 참조하기때문에 base는 a가 됨 