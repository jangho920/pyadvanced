# 시각화 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("자료실/data.csv")

#df.plot()
#df.plot(kind='scatter', x='Duration', y='Calories')
#df.plot(kind='scatter', x='Duration', y='Pulse')
#df.plot(kind='scatter', x='Duration', y='Maxpulse')
df['Duration'].plot(kind='hist') #분포 다이어그램

plt.show()

