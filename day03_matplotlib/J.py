import matplotlib.pyplot as plt
import numpy as np

yp = np.array([30, 20, 40, 10])
soolabels = ["tiger", "rabbit", "lion", "mouse"]
sooexplode = [0.3, 0, 0.1, 0]
soocolors = ["red", "green", "blue", "yellow"]

#plt.pie(yp, labels=soolabels) #startangle: x축 right ,  counterclockwise(반시계방향)
#plt.pie(yp, labels=soolabels, startangle=90)
plt.pie(yp, labels=soolabels, explode=sooexplode, colors=soocolors)
#plt.legend()
plt.legend(title="Animals")
plt.show()