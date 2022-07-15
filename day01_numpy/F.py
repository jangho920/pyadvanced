import numpy as np
a = np.array([1,2,3,4,5])
print(a.dtype) #int32

b = np.array(["tiger", "lion", "rabbit"])
print(b.dtype) #<U6

c = np.array([1,2,3,4,5], dtype='S')
print(c)
print(c.dtype)

d = np.array([1,2,3,4,5], dtype='i8')
print(d)
print(d.dtype) #int64

e = np.array([1.3, 2.5, 3.8])
#e2 = e.astype('i') #데이터타입 컨버팅 메소드
e2 = e.astype(int) #데이터타입 컨버팅 메소드
print(e2)
print(e2.dtype) #int32

f = np.array([-2, 0, 1, 5])
f2 = f.astype(bool)
print(f2) #[ True False  True  True]
print(f2.dtype) #bool



