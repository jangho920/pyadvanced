import matplotlib.pyplot as plt
import seaborn as sns 
from numpy import random as r 

x = r.normal(size=2000)
print(x)
sns.distplot(x)
plt.show()
