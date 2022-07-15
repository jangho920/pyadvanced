import matplotlib.pyplot as plt
import numpy as np

yp = np.array([2, 8, 1, 9, 5, 7])

#(1) linestyle
#plt.plot(yp, linestyle="dotted")
#plt.plot(yp, ls=":") #dotted

#plt.plot(yp, linestyle="dashed")
#plt.plot(yp, ls="--") #dashed

#plt.plot(yp, ls='-') #solid (기본값) 
#plt.plot(yp, ls='-.') #dashdot

#(2) color
#plt.plot(yp, color='r') 
#plt.plot(yp, color='#0cf0f7')  #임의의 컬러

#(3) linewidth
#plt.plot(yp, color='r', linewidth='15')

#(4) Multi Lines
yp2 = np.array([4, 7, 2, 8, 6, 3])
plt.plot(yp) #1번째
plt.plot(yp2) #2번째 

plt.show()