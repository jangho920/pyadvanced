import matplotlib.pyplot as plt
import numpy as np

yp = np.array([2, 8, 1, 9, 5, 7])
#plt.plot(yp, marker='o')
#plt.plot(yp, marker='*')
#plt.plot(yp, marker='D')

#plt.plot(yp, 'o:r') # marker와 color 
plt.plot(yp, 'o:g')

plt.plot(yp, 'o-.') # marker와 line  

plt.plot(yp, 'o-.', ms=25) # marker와 line과 size 

plt.plot(yp, 'o-.', ms=25, mec='r', mfc='y') # marker와 line과 size와 마커테두리색과 마커색 

plt.plot(yp, 'o-.', ms=25, mec='#23db98', mfc='#eb15cb') # colorpicker

plt.show()