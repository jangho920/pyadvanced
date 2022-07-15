import pandas as pd

#(1) 읽기 
df = pd.read_json("자료실/data.json")
#print(df)
print(df.to_string())

df.set_index('Duration', inplace=True) # Duration 열을 index로 지정
print(df)

#(2) 쓰기 
df.to_excel("자료실/output/data_json.xlsx")
df.to_csv("자료실/output/data_json.csv")
