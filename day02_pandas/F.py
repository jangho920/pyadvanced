import pandas as pd

#(1) 읽기 
df = pd.read_excel("자료실/data.xlsx", engine="openpyxl")
print(df)

df.set_index('Duration', inplace=True) # Duration 열을 index로 지정
print(df)

#(2) 쓰기
df.to_csv("자료실/output/data_xlsx.csv")
#df.to_json("자료실/output/data_xlsx.json") #에러발생 why?



#(3) 기타 엘셀 읽기 테스트 
'''
df1 = pd.read_excel("자료실/남북한발전전력량.xlsx", engine="openpyxl")
df2 = pd.read_excel("자료실/경기도인구데이터.xlsx", engine="openpyxl")
df3 = pd.read_excel("자료실/서울지역 대학교 위치.xlsx", engine="openpyxl")
df4 = pd.read_excel("자료실/시도별 전출입 인구수.xlsx", engine="openpyxl")
print(df1)
print(df2)
print(df3)
print(df4)
'''