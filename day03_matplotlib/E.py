import matplotlib.pyplot as plt
import numpy as np

xp = np.array([60, 60, 60, 45, 45, 60, 60, 45, 30])
yp = np.array([409, 479, 340, 282, 406, 300, 374, 253, 195])
plt.plot(xp, yp)

f1 = {'family':'Arial Black', 'color':'red', 'size':18}
f2 = {'family':'serif', 'color':'green', 'size':14}

plt.title("< Duration and Calories >", fontdict=f1, loc="right")
plt.xlabel("Duration", fontdict=f2)
plt.ylabel("Calories", fontdict=f2)

#plt.grid() #가로와 세로줄 
#plt.grid(axis='x') #세로줄 
#plt.grid(axis='y') #가로줄
plt.grid(color='green', linestyle="--", linewidth=0.7) 

plt.show()
