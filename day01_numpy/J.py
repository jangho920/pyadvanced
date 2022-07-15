import numpy as np

a = np.array([1,2,3,4,5]) #1차원
for x in a:
    print(x)
print()

b = np.array([[1,2], [3,4]]) #2차원
for x in b:
    for y in x:
        print(y)    
print()

c = np.array([[[1,2], [3,4]], [[5,6], [7,8]]]) #3차원
for x in c:
    for y in x:
        for z in y:
            print(z)
print()

for x in np.nditer(c):  # 이 방법도 있음
    print(x)
print()

d = np.array([1,2,3,4,5])  
for i, x in np.ndenumerate(d):
    print(i, x)
print()

e = np.array([[1,2], [3,4]]) #2차원    
for i, x in np.ndenumerate(e):
    print(i, x)
print()

