import pandas as pd

# 동일한 값을 가진 row들을 제거   
df = pd.read_csv('자료실/data.csv')
print(df.to_string())
print()

x = df.corr() # Correlations : 상관관계계수
print(x)