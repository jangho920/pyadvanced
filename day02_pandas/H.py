import pandas as pd

# empty cell 제거  
df = pd.read_csv('자료실/dirtydata.csv')
print(df.to_string())
print()

df2 = df.dropna() #empty cell을 가진 row들을 제거해서 '새로운 df생성' 
print(df2.to_string())
print()

df.dropna(inplace=True) #'원본의 df'에서 empty cell을 가진 row들을 제거
print(df.to_string())

