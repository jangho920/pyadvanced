import pandas as pd

# empty cell 채움  
df = pd.read_csv('자료실/dirtydata.csv')
print(df.to_string())
print()

#df.fillna(200, inplace=True) # 모든 empty cell에 200을 채움 
#print(df.to_string())
#print()

#df["Calories"].fillna(200, inplace=True) # 모든 empty Calories 셀만에 200을 채움 
#print(df.to_string())
#print()

#x = df["Calories"].median() #291.2 => mid point value
#x = df["Calories"].mean() #304.68 => average value
x = df["Calories"].mode()[0] #300.0 => most common value
df["Calories"].fillna(x, inplace=True)
print(df.to_string())
