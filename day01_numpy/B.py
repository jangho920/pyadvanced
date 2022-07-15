import numpy as np

a = np.array(12) #0차원 
b = np.array([1, 2, 3, 4]) #1차원 
c = np.array([[1,2],[3,4]]) #2차원 
d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) #3차원

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#print(d)