import numpy as np

a = np.array([1,2,3,4])
b = [True, True, False, True]
c1 = a[b]
print(c1) #[1 2 4]
print()

#c2 = a>2 #[False False  True  True]
c2 = a%2==0 #[False  True False  True]
print(c2)
c3 = a[c2]
print(c3)