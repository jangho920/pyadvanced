import pandas as pd

#(1) 읽기 
df = pd.read_csv('자료실/data.csv')
#print(df.to_string()) #전체row 출력 
#print(df) #header 5개, tailer 5개 

#print(pd.options.display.max_rows) # 현재 디플레이되는 최대 row갯수 설정 
pd.options.display.max_rows = 169 # 총 rows 갯수가 169개이므로 모두 출력 
pd.options.display.max_rows = 168 # 총 rows 갯수(169개) 보다 적으므로 head와 tail로 나눠출력
print(df) #head와 tail 각각 5개씩 출력
print(df.head(10)) #head를 10개 출력  
print(df.tail(10)) #tail를 10개 출력
print(df.head()) #head를 5개 출력 
print(df.tail()) #tail를 5개 출력
print(df.info()) #df의 컬럼정보와 데이터타입 출력 ( 오라클의 desc 와 비슷 )

df.set_index('Duration', inplace=True) # Duration 열을 index로 지정
#print(df)

#(2) 쓰기 
df.to_excel("자료실/output/data_csv.xlsx")
#df.to_json("자료실/output/data_csv.json")  #에러발생 why?

