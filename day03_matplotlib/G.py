#scatter
import matplotlib.pyplot as plt
import numpy as np

xp = np.array([60, 60, 60, 45, 45, 60, 60, 45, 30])
yp = np.array([409, 479, 340, 282, 406, 300, 374, 253, 195])
#plt.plot(xp, yp) #선
#plt.scatter(xp, yp) #점 
plt.scatter(xp, yp, color='gray') 

xp = np.array([30, 30, 45, 45, 45, 60, 60, 60, 75, 75])
yp = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#plt.scatter(xp, yp, color='pink') 
'''
colors = np.array(["red", "green", "blue", "yellow", "pink", 
                   "orange", "cyan", "magenta", "brown", "gray"])
plt.scatter(xp, yp, c=colors)
'''
colors = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
sizes = np.array([50, 80, 90, 20, 30, 200, 250, 70, 500, 30])
plt.scatter(xp, yp, c=colors, cmap='viridis', s=sizes, alpha=0.3)
plt.colorbar()

plt.show()