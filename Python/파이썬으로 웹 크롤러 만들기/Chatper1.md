### 1.2.2 BeautifulSoup 실행
---
- BeautifulSoup 라이브러리에서 가장 널리 쓰이는 객체는 물론 BeautifulSoup 객체이다.
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
```

- 출력결과 `<h1>An Interesting Title</h1>`
