import pandas as pd

#DataFrame: 2차원 테이블 데이터의 구조 
a = {
    "calories": [400, 300, 350], 
    "duration": [50, 35, 45]
}
df1 =  pd.DataFrame(a)
print(df1)
print() 
print(df1.loc[1]) #index 1의 row를 추출 
print()
print(df1.loc[[0,1]]) #index 0이상 1이하의 row를 추출 
print()

df2 = pd.DataFrame(a, index=["d1", "d2", "d3"])
print(df2)
print(df2.loc["d2"])
