import pandas as pd

# Wrong Data 변경 / 삭제  
df = pd.read_csv('자료실/dirtydata.csv')
print(df.to_string())
print()

# (1) 임의값으로 셋팅 
#df.loc[7, 'Duration'] = 60
#print(df.to_string())
#print()

# (2) 반복문을 돌려서 특정값 셋팅 
for x in df.index:
    if df.loc[x, 'Duration'] > 150:
        df.loc[x, 'Duration'] = 150
print(df.to_string())
print()

# (3) 반복문을 돌려서 특정값 셋팅 
for x in df.index:
    if df.loc[x, 'Duration'] > 100:
        df.drop(x, inplace=True)
print(df.to_string())
print()