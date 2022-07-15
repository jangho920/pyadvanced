import numpy as np

a = np.array([[1,2,3], [4,5,6]])
print(a.shape) #(2, 3)

b = np.array([1,2,3,4,5], ndmin=3) #3차원배열을 만들어라
print(b)
print(b.shape) #[[[1 2 3 4 5]]] -> (1, 1, 5) : 2차원 1개, 1차원 1개, 그 안에 5개

