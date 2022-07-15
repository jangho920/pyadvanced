from numpy import random as r
import numpy as np

a = [1,2,3,4,5]
x = np.array(a)
print(x)
y = r.permutation(x) #혼합: 원본배열(x)은 바꾸지않고, 변경된 새로운 배열(y)이 생성 
print(x)
print(y)
print()

r.shuffle(x) #혼합 : 원본배열을 변경시킴 
print(x)

