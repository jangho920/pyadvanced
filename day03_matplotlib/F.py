#subplot()으로 배치레이아웃과 위치지정 

import matplotlib.pyplot as plt
import numpy as np

yp1 = np.array([2, 8, 1, 9, 5, 7])
plt.subplot(1, 2, 1) # 1행2열중 1번째
#plt.subplot(2, 1, 1)  # 2행1열중 1번째
plt.plot(yp1)
plt.title("Title1")

yp2 = np.array([1, 9, 2, 8, 3, 5])
plt.subplot(1, 2, 2) # 1행2열중 2번째
#plt.subplot(2, 1, 2) # 2행1열중 1번째
plt.plot(yp2)
plt.title("Title2")

plt.suptitle("Top Title")
plt.show()