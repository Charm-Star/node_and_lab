import openai
import pandas as pd
import os


# 엑셀 파일 경로 및 열 이름 설정
excel_file = "C:/Users/User/Desktop/project/TEST color.xlsx"
column_name1 = "종합"


# 엑셀 파일 읽어오기
df = pd.read_excel(excel_file)

# 원하는 열의 데이터만 추출하기
selected_column1 = df[column_name1]



# 결과 출력


openai.api_key = "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"

model_engine = "text-davinci-003" # "Davinci" 모델 엔진 ID

#
response=[]

for i in selected_column1:


  
  prompt = str(i) + """ 이 내용에서 작업자의 부상 부위를 추출해 줘. 부상 부위 정보가 없으면 "@@"를 출력해줘 """

# API 호출
  completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      temperature=0,
      max_tokens=2000,
      n=1,
  )
  print(i)
  print(completions.choices[0].text)
  if "@@" in completions.choices[0].text: # 수정필요 
    com = openai.Completion.create(
      engine = model_engine,
      prompt = str(i) + """이 내용에서 부상부위를 추측해서 "추측결과:" 형식으로 출력해줘 """,
      temperature = 0,
      max_tokens=2000,
      n=1,
      
    )
    
    print(com.choices[0].text)
    response.append(com.choices[0].text)
    continue
  response.append(completions.choices[0].text)

# 엑셀파일에 입력하기
num = 0
for res in response:

  df.loc[num, 'GPT-부상부위'] = res
  num+=1


df.to_excel('TEST_result.xlsx', index=False)

