# -*- coding: utf-8 -*-
"""test

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sI8jWxFllTTzbqnnNDteWC6AG5l_pftt
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install openai

!pip install tiktoken

!pip install newspaper3k

# imports
import ast  # for converting embeddings saved as strings back to arrays
import openai  # for calling the OpenAI API
import pandas as pd  # for storing text and embeddings data
import tiktoken  # for counting tokens
from scipy import spatial  # for calculating vector similarities for search
import re

# models
EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"
openai.api_key = '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'

"""## 질문 임베딩

## 사용자 쿼리 기반 정보 검색

직접 크롤링
"""

from newspaper import Article
#news_url = "https://www.wikitree.co.kr/articles/900115"
news_url = "https://sports.news.naver.com/news?oid=108&aid=0003195169"

#article 클래스를 설정하고, 클래스 안에 url을 넣어준다.
article = Article(news_url, language='ko')

#다운로드와 파싱 제공
article.download()
article.parse()

article.title # 기사의 제목
text = article.text # 기사 본문

import re
re.sub(r"<[^>]+>\s+(?=<)|<[^>]+>", "", text).strip()

"""네이버 뉴스 open api 활용"""

import os
import sys
import urllib.request

client_id = "mlh83KWXXlaNBjyKSkwl"
client_secret = "FXklZGr5en"
encText = urllib.parse.quote("2024 대학수학능력시험")

#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

"""뉴스토어 api

Bing search services

### GPT api
"""

from openai import OpenAI
client = OpenAI()

def generate_data(openai : any, text: str, num : int) -> str:
    response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=[
          #시스템 메시지는 어시스턴트의 동작을 설정(선택사항)
        {"role": "system", "content": "generate the JSON data"},
          #어시스턴트가 응답할 수 있는 요청이나 의견을 제공
        {"role": "user", "content": f"""
        #######prompt########
        Generate {num} pieces of JSON data that follow the guidelines and examples below.

        {prompt}

         """},
      ]
    )
    return response.choices[0].message.content

prompt = """
"""

#생성할 데이터 숫자
total_num = 50
num_per_gen = 10 #한 프롬프트에서 생성할 데이터 수
itr_num = int(total_num/num_per_gen)

#json 저장할 리스트
data = []


for i in tqdm(range(itr_num)):
  print(f'\n-----------------------생성 시작 {i+1}/{itr_num}-----------------------\n')

  #생성 요청
  answer = generate_data(openai,prompt,num_per_gen)
  print(answer)


  # '{'와 '}'를 기준으로 텍스트를 분할
  split_text = re.findall(r'\{.*?\}', answer, re.DOTALL)

  # 각 문자열을 딕셔너리로 변환
  dict_data = [json.loads(item) for item in split_text]

  # 리스트에 추가
  data.append(dict_data)


  # JSON 파일로 저장
  print(f'\n-----------------------저장 중 {i+1}/{itr_num}-----------------------\n')

  path = '/content/drive/MyDrive/4학년1학기/SAI/프로젝트/test_data.json'
  with open(path, 'w', encoding='utf-8') as file:
      json.dump(data, file, ensure_ascii=False, indent=4)

  print(f'\n-----------------------저장 완료 {i+1}/{itr_num}-----------------------\n')

  print(f'\n-----------------------생성 종료 {i+1}/{itr_num}-----------------------\n')



# search function
def strings_ranked_by_relatedness(
    query: str, #쿼리문 입력
    df: pd.DataFrame, #데이터프레임
    relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y), #코사인 유사도 계산
    top_n: int = 100
) -> tuple[list[str], list[float]]:
    """Returns a list of strings and relatednesses, sorted from most related to least.
    """
    #가장 관련성이 높은 것부터 가장 낮은 것까지 정렬된 문자열 및 관련성 목록을 반환합니다.
    query_embedding_response = openai.Embedding.create( #쿼리문 임베딩
        model=EMBEDDING_MODEL,
        input=query,
    )
    query_embedding = query_embedding_response["data"][0]["embedding"] #쿼리문 임베딩
    strings_and_relatednesses = [ #text와 유사도 계산
        (row["text"], relatedness_fn(query_embedding, row["embedding"]))
        for i, row in df.iterrows()
    ]
    strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
    strings, relatednesses = zip(*strings_and_relatednesses)
    return strings[:top_n], relatednesses[:top_n]

