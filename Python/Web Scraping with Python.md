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