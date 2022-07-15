from numpy import random as r

a = [1, 2, 3, 4]
b = [0.2, 0.3, 0.5, 0.0]
x1 = r.choice(a, p=b, size=100)
print(x1)
print()

x2 = r.choice(a, p=b, size=(3,4))
print(x2)
