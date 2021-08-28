# 개요

1. 웹 스크래핑과 크롤링의 기본 설명
2. 고급 주제 몇 가지



## 웹 스크래핑이란?

---

- 데이터를 수집하는 작업 전체를 말한다.

BeautifulSoup을 활용한 웹 스크래핑 예제

```python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# 문제가 생기면 None객체를 반환함
def getTitle(url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
  try:
    bs = BeautifulSoup(html.read(), 'html.parser')
    title = bs.body.h1
  except AttributeError as e:
    return None
  return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title = None:
  print('Title could not be found')
else:
  print(title)
```

- **예외처리를 철저하게 만들어두면 빠르고 믿을 수 있는 웹 스크래퍼를 만들 수 있다.**



## Chapter2 - 고급 HTML 분석

---

이 장에서는 복잡한 HTML 페이지를 분석해서 원하는 정보만 추출하는 방법을 알아보겠습니다.

- 별로 좋아 보이지는 않는 코드 (사이트의 관리자가 사이트를 조금만 수정하면 동작이 멈춤)

  `bs.findAll('table')[4].find_all('tr')[2].find('td').find_all('div')[1].find('a')`

  

- 보다 나은 방법

  1. '페이지 인쇄'같은 링크를 찾거나, 더 나은 HTML 구조를 갖춘 모바일 버전 사이트 찾아보기

  2. 자바스크립트 파일에 숨겨진 정보 찾아보기

  3. 중요한 정보는 페이지 타이틀에 있을 때가 대부분이지만, 원하는 정보가 페이지 URL에 들어있을 때도 있다.

     

**데이터가 깊숙이 있거나 정형화되지 않을수록, 코드부터 짜려고 달려들었다간 낭패를 본다.**



### 다시 BeautifulSoup

---

이 섹션에서는 

1. 속성을 통해 태그를 검색하는 법
2. 태그 목록을 다루는 법
3. 트리 내비게이션을 분석하는 법

에 대해 알아본다.

- 1장과 마찬가지인 기본적인 Bs4 프로그램

  ```python
  from urllib.request import urlopen
  from bs4 import BeautifulSoup
  
  html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
  bs = BeautifulSoup(html, 'html.parser')
  
  # <span class="green"></span> 태그에 있는 텍스트만 선택해서 고유명사로 이루어진 파이썬 리스트를 추출한다.(findAll은 대단히 유연한 함수이며 매우 자주 사용된다.)
  nameLise = bs.findAll('span', {'class': 'green'})
  for name in nameList:
    print(name.get_text())
    
    
  # .get_text()는 현재 문서에서 모든 태그를 제거하고 유니코드 텍스트만 들어 있는 문자열을 반환한다.
  # 예를 들어 하이퍼링크, 문단, 기타 태그가 여럿 들어있는 텍스트 블록에 사용하면 태그없는 텍스트만 남는다.
  ```

  

#### 2.2.1 find()와 findAll()

---

두 함수는 bs4에서 가장 자주 쓰는 함수이다.
이 함수를 쓰면 HTML 페이지에서 원하는 태그를 다양한 속성에 따라 쉽게 필터링할 수 있다.

- 두 함수는 거의 비슷한데, bs4 문서의 함수 정의만 봐도 알 수 있다.

  ```python
  findAll(tag, attributes, recursive, text, limit, keywords)
  find(tag, attributes, recursive, text, keywords)
  ```

- 다음 코드는 문서의 모든 헤더 태그 리스트를 반환한다.

  `bs.findAdd({'h1', 'h2', 'h3', 'h4', 'h5', 'h6'})`

- 다음 코드는 HTML 문서에서 녹색과 빨간색 span 태그를 모두 반환한다.

  `bs.findAll('span', {'class':{'green', 'red'}})`

- 태그에 둘러싸인 'the prince'가 몇 번 나타났는지 보려면 이전 예제의 findAll()을 다음과 같이 고치면 된다.

  ```python
  nameList = bs.findAll(text = 'the prince')
  print(len(nameList)) # 7
  ```

- limit 매개변수는 당연히 findAll에만 쓰인다. find는 findAll을 호출하면서 limit을 1로 지정한 것과 같다. 이 매개변수는 페이지의 항목 처음 몇 개에만 관심이 있을 때 사용한다.

  `title = bs.findAll(id='title', class_='text')`

#### 2.2.2 기타 bs4 객체

---

지금까지 bs 라이브러리의 두 가지 객체를 설명했다.

1. BeautifulSoup 객체 - bs와 같은 형태로 사용했다.

2. Tag 객체 - 리스트 호출 또는 BeautifulSoup 객체에 find와 findAll을 호출해서 또는 다음과 같이 탐색해 들어가서 얻는다.

   `bs.div.h1`

하지만 두 가지의 객체가 더 있다. 널리 쓰이지는 않지만 알아둘 가치는 있다.

1. NavigableString 객체 - 태그 자체가 아니라 태그 안에 들어 있는 텍스트를 나타낸다. 일부 함수는 NavigableStrings를 다루거나 반환한다.
2. Comment 객체 - 주석 태그 안에 들어있는 HTML 주석 (<!-- 이런 주석 -->)을 찾는 데 사용한다.

이 책을 쓰는 시점에서 BeautifulSoup 라이브러리에는 이 네가지 객체가 전부이다.