import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a.shape) #(10,)

a2 = a.reshape(4,3) #2차원으로 변경 
print(a2)
print(a2.shape) #(4, 3)

a3 = a.reshape(2,3,2) #3차원으로 변경 
print(a3)
print(a3.shape) #(2, 3, 2)
print(a3.base) #원본을 참조했음 : view()됨 
print()

b = np.array([[[1,2], [3,4]], [[5,6], [7,8]]]) 
b2 = b.reshape(-1) #[1 2 3 4 5 6 7 8] #평탄화: 1차원로 변경
print(b2)

