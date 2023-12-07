
### 개요
> 인터넷 주소를 넣고 실행하여 데이터를 받아 오는 것을 ‘크롤링’이라 함
> 받아온 데이터에서 필요한 내용만 추출하는 것을 ‘파싱’이라고 함

> - urlib는 파이썬에서 데이터를 받아오는 기능의 패키지(내부 라이브러리)
> - BeautifulSoup은 데이터를 추출하는데 필요한 기능이 들어있는 파싱 라이브러리(외부 라이브러리)

- 웹에서 데이터를 받아오려먼 http request를 보내 받아와야 함
- urlib.request : 웹의 특정 주소로 요청을 보내는 기능
- urlib.request.urlopen : 페이지를 불러옴
```python
import urllib.request
import bs4

url = "https://www.naver.com/"

# html 변수에 텍스트 형식으로 페이지의 데이터가 문자열의 형태로 저장됨
html = urllib.request.urlopen(url)

# 데이터를 파싱하기 위해 bs4에 데이터를 넣은 후 파이썬에서 가공할 수 있는 형태로 만듦
bs_obj = bs4.BeautifulSoup(html, "html.parser")

print(html.read())
```
