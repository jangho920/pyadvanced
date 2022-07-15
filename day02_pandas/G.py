import pandas as pd

df = pd.read_html("자료실/data.html")
print(df)
print()

print(len(df)) #table태그의 갯수
print()

print(df[0])
print()
print(df[1])
print()

df[0].set_index(['c0'], inplace=True)
print(df)
print()

df[1].set_index(['name'], inplace=True)
print(df)