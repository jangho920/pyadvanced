import matplotlib.pyplot as plt
from numpy import random as r

#x = r.normal(size=(2,3)) # 2행3열 랜덤배열 ( 0이 기준값 )
#x = r.normal(size=100) # 100개의 램덤배열 ( 0이 기준값 )
x = r.normal(100, 10, 500) #( 기준값, 표준편차, 생성갯수 ) 
#print(x)

plt.hist(x) #분포 다이이그램 
plt.show()
