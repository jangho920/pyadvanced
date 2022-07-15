import pandas as pd

# Wrong format 변경 / 삭제  
df = pd.read_csv('자료실/dirtydata.csv')
print(df.to_string())
print()

df['Date'] = pd.to_datetime(df['Date']) # 일반적인 날짜포멧으로 '변경'
print(df.to_string())
print()

df.dropna(subset=['Date'], inplace=True) # 22라인(NaN 또는 NaT)의 row '삭제'
print(df.to_string())
print()
 