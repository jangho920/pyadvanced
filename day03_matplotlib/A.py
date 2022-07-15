#import matplotlib
#print(matplotlib.__version__) #3.5.2


import matplotlib.pyplot as plt
import numpy as np

xp = np.array([0, 5])
yp = np.array([0, 300])
print(xp)
print(yp)

#plt.plot(xp, yp) #line ( O )
plt.plot(xp, yp, 'o') # line ( X )
plt.show()