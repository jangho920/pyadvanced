import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
b1 = np.array_split(a, 3) 
print(b1) #[array([1, 2]), array([3, 4]), array([5, 6])]
print(b1[0])
print(b1[1])
print(b1[2])
print()

b2 = np.array_split(a, 4) 
print(b2) #[array([1, 2]), array([3, 4]), array([5]), array([6])]


c = np.array([[1,2],[3,4],[5,6],[7,8],[9,10], [11,12]])
d1 = np.array_split(c, 3) #방법1
print(d1) 
d2 = np.vsplit(c, 3) #방법2
print(d2)


