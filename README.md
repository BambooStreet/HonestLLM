# HonestLLM

HonestLLM is a tool that allows users to verify the accuracy of the output of AI models and
provides information about the reason behind them.

The goal of the project is to develop technologies to determine the authenticity of the output of AI models and to prevent hallucinations. Users will be able to visually check the reliability of their answers using a fact-based database.

Through this, we will create a safe and reliable artificial intelligence environment and a more certain and advanced future.

## Installation

### System requirements

- Python 3.8 or later.
- MacOS, Windows are supported.

### GPT Plugin
To get to the Chat GPT plugin, search for it in the following search bar.

![plugin_use](./img/Plugin_use.png)

### Local
To use it in your local environment, please obtain an API key from the site below.

* OpenAi API : https://platform.openai.com/api-keys
* Naver News API : https://developers.naver.com/docs/serviceapi/search/news/news.md

## Usage

### In Plugin
It is waiting to be reviewed in the OPEN AI waitlist.

<img src="./img/installation.png" width="500" height="300"/>

### In Local
In Local environment, it utilizes the API KEY you were issued. Then, using our code, we can see the appropriate output for the user's question.

When writing your question, try to make your keywords stand out as much as possible!

## Example

### input
For example, you might ask for recent news stories about Heung Min Son.

```python
answer = generate_answer('손흥민의 최근 뉴스들을 알려줘')
```

### output
HonestLLM extracts keywords from user questions and informs you about them based on recent news. 

```python
answer
손흥민 선수에 관한 최근 뉴스에는 다음과 같은 내용이 포함되어 있습니다:

1. 주장으로서의 역할: 영국 매체 'TBR 풋볼'에 따르면, 엔제 포스테코글루 감독은 이번 시즌을 앞두고 손흥민 선수를 토트넘의 새로운 주장으로 임명하였습니다. 손흥민 선수는 주장으로서 첫 연설을 할 때 크게 긴장했다고 말했으며, 이는 그가 경험한 가장 긴장된 순간 중 하나였습니다.

2. 팀의 분위기 변화: 토트넘에서 주장이 된 이후, 손흥민 선수는 선수들을 하나로 뭉치게 하는 리더십을 발휘하고 있습니다. 경기장 밖에서도 선수들과 좋은 관계를 유지하며 좋은 경기력을 선보이고 있습니다. 이로 인해 토트넘은 시즌 초반 좋은 흐름을 타고 있지만, 최근에는 리그 2연패에 빠졌으며 승점 26으로 4위에 위치해 있습니다.

이 외에도, 토트넘은 현재 공격수 부문에서 변화가 있을 수 있는 상황에 놓여있습니다. 특히 히샬리송 선수가 사우디아라비아로 이적할 가능성이 언급되며, 토트넘은 새로운 공격수 영입을 고려하고 있는 상황입니다.

손흥민 선수 개인적으로는 토트넘에서 중요한 역할을 수행하고 있으며, 새로운 주장으로서 팀의 통합과 성과 향상을 위해 중요한 역할을 하고 있다는 점이 강조되고 있습니다.
```

## Methods

### Embedding
Embed user input and match it against a news article.Calculate the similarity between the user's question and the article through embedding. 

<img src="./img/embeddings_visual.webp" width="500" height="300"/>

https://platform.openai.com/docs/guides/embeddings/limitations-risks

### Use Naver News API
<p><img src="./img/naver.png"></p>


https://developers.naver.com/docs/serviceapi/search/news/news.md

Using the NAVER News API, you can select articles that are most similar to the user's question and have a conversation with LLM based on that.

### Calculate cosine similarity
```python
def strings_ranked_by_relatedness(
    query: str, #쿼리문 입력
    df: pd.DataFrame, #데이터프레임
    relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y), #코사인 유사도 계산
    top_n: int = 100
) -> tuple[list[str], list[float]]:
    """Returns a list of strings and relatednesses, sorted from most related to least.
    """

    query_embedding = get_embedding(query) #쿼리문 임베딩
    strings_and_relatednesses = [ #text와 유사도 계산
        (row["title"], row["text"], relatedness_fn(query_embedding, row["title_embedding"]))
        for i, row in df.iterrows()
    ]
    strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
    title_strings, text_strings, relatednesses = zip(*strings_and_relatednesses)
    return title_strings[:top_n], text_strings[:top_n], relatednesses[:top_n]
```

### Extract relevant article titles
```python
relatedness=0.782
"토트넘, 이건 정말 기회야!....'사우디 1타깃' 히샬리송, 제발로 걸어 나갈 수도"
relatedness=0.853
"SON 이런 모습 처음이야! 손흥민이 가장 긴장했던 순간은?"
relatedness=0.787
"반려견 애정 영부인, 유머 있는 대통령…유럽 매체들 집중 보도"
relatedness=0.775
"황의조, 귀국 대신 바로 영국으로 떠나"
relatedness=0.862
"손흥민은 쏘니, 황희찬은 차니!..."재계약 희망적" 울버햄튼 감독이 직접 나섰다"
```

Answer by selecting the most similar articles. For a detailed example, see the example below.
This way, you can expect an answer based on accurate evidence.

HonestLLM gives you the experience of having a trendy conversation with an LLM.

## Licenses

Apache License 2.0  

## Authors

- 18011093 황성태
    
- 18011543 박지환
  
- 19010976 김민재
  
- 19012022 홍석주
