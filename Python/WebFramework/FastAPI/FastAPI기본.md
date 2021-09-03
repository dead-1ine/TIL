# 개요

---

"FastAPI 프레임워크, 고성능, 간편한 학습, 빠른 코드 작성, 준비된 프로덕션"

- FastAPI는 현대적이고, 빠르며(고성능), 파이썬 표준 타입 힌트에 기초한 Python3.6+의 API를 빌드하기 위한 웹 프레임워크이다.
  - 빠름: (Starlette과 Pydantic 덕분) NodeJS 및 Go와 대등할 정도로 매우 높은 성능. 
  - 빠른 코드 작성: 약 200%에서 300%까지 기능 개발 속도 증가.
  - 적은 버그: 개발자에 의한 에러 약 40% 감소.
  - 직관적: 훌륭한 편집기 지원. 모든 곳에서 자동완성. 적은 디버깅 시간.
  - 쉬움: 쉽게 사용하고 배우도록 설계. 적은 문서 읽기 시간.
  - 짧음: 코드 중복 최소화. 각 매개변수 선언의 여러 기능. 적은 버그.
  - 표준 기반: API에 대한 개방형 표준 기반

### FastAPI의 기본 서비스

---

- Swagger : http://localhost:8000/docs

- ReDoc : http://localhost:8000/re

- http://localhost:8000/openapi.json



### 설치

---

`pip install fastapi`
`pip install uvicorn[standard]`



### HTTP 기본 메소드

---

- POST: 데이터를 생성하기 위해
- GET: 데이터를 읽기 위해
- PUT: 데이터를 업데이트하기 위해
- DELETE: 데이터를 삭제하기 위해



### 예제 1

---

> #### 요약 
>
> - FastAPI 임포트
> - app 인스턴스 생성
> - `app.get("/")`: 경로 동작 데코레이터 작성
> - `def root():` : 경로 동작 함수 작성
> - `uvicorn main:app --reload` : 개발 서버 실행

- main.py 파일 만들기
  - @something 문법은 파이썬에서 "데코레이터"라고 부른다.
  - "데코레이터" 아래의 함수는 그걸 이용해 무언가를 한다.

```python
from typing import Optional
from fastapi import FastAPI

# FastAPI의 인스턴스(이후 .get이나 uvicorn에서 사용됨)
app = FastAPI()

# 경로 동작 데코레이터 : "/" 경로에서 아래의 함수로 GET 동작을 하겠다는 의미
@app.get("/")
def read_root():
  # Contents 반환
  return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
  return {"item_id": item_id, "q": q}
```

- 서버 실행

  `uvicorn main:app --reload`

- 브라우저로 확인하기 : http://localhost:8000/items/5?q=somequery (GET)

- JSON 응답 : {"item_id" : 5, "q" : "somequery"}

- 대화형 API 문서 확인하기 : http://localhost:8000/docs

- 대안 API 문서 확인하기 : http://localhost:8000/redoc



### 예제 2

---

- PUT 요청 만들기

```python
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Optional[bool] = None
    
@app.put("/items/{item_id}")    
def update_item(item_id: int, item: Item):
  return {"item_name": item.name, "item_id": item_id}
```

- 서버 reload : `uvicorn main:app --reload`
- Swagger에서 "Try it out"을 활용해 매개변수를 전달하고 직접 API와 상호작용할 수 있음
- 그 후 "Execute"를 통해, 사용자 인터페이스는 API와 통신하고 매개변수를 전달하여 그 결과를 화면에 표시함
