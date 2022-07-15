import numpy as np

a = np.array([1,2,3,4,5,3,3])
x = np.where(a==3)
print(x) #[2, 5, 6]
y = np.where(a%2==0)
print(y) #[1, 3]
z = np.sort(a)
print(z)
print()

b = np.array(['tiger', 'lion', 'rabbit'])
print(np.sort(b))

c = np.array([True, False, True])
print(np.sort(c))

d = np.array([[2,1,3], [5,4,6]])
print(np.sort(d))