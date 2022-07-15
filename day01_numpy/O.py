from numpy import random as r

x1 = r.randint(100) #0 ~ (n-1)
print(x1)

x2 = r.rand() #0 ~ 1 실수
print(x2)

x3 = r.randint(100, size=5) #5개 요소를 가진 1차원배열 
print(x3)
print()

x4 = r.randint(100, size=(3,5)) #(3,5)개 요소를 가진 2차원배열 
print(x4)

x5 = r.rand(5) #0~1실수 5개의 요소를 가진 1차원배열
print(x5)

x6 = r.rand(3, 5) #0~1실수 (3,5)개를 요소를 가진 2차원배열
print(x6)

x7 = r.choice([1, 2, 3, 4])
print(x7)

x8 = r.choice([1, 2, 3, 4], size=(3,4))
print(x8)