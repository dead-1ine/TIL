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
> - `app.get("/")`: path operation decorator 작성
> - `def root():` : path operation function 작성
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



### 경로 매개변수

---

- 파이썬과 동일한 문법으로 "매개변수" 또는 "변수"를 경로에 선언할 수 있다.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
  return {"item_id" : item_id}
```

- 경로 매개변수 item_id의 값은 함수의 item_id 인자로 전달된다.

  이 예제를 실행하고 http://localhost:8000/items/foo로 이동하면 다음 응답을 볼 수 있다.

  `{"item_id" : "foo"}`



### 타입이 있는 매개변수

---

- 파이썬 기본 문법과 동일하게 경로 매개변수의 타입을 선언할 수 있다.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
  return {"item_id" : item_id}
```

- 이 예제를 실행하고 http://localhost:8000/items/3로 이동하면 다음 응답을 볼 수 있다.

  `{"item_id" : 3}` - 선언된 타입으로 자동 파싱됨

- 만약 int형으로 파싱될 수 없다면 다음 에러가 나옴

- 오류는 검증을 통과하지 못한 지점까지 정확하게 명시함

```json
{
  "detail" : [
    {
      "loc" : [
        "path",
        "item_id"
      ],
      "msg" : "value is not a valid interger",
      "type" : "type_error.integer"
    }
  ]
}
```

### Pydantic

---

- 모든 데이터 검증은 Pydantic에 의해 내부적으로 수행되므로 이로 인한 모든 이점을 얻을 수 있다.
- `str, float, bool`과 다른 복잡한 데이터 타입 선언을 할 수 있다.



### 순서 문제

---

- 경로 동작을 만들 때 고정 경로를 갖고 있는 상황을 만날 수 있다.
- 경로 동작은 순차적으로 평가되기 때문에 `/users/me`를 사용한다면 `/users/{user_id}`보다 먼저 선언해야 한다.
  그렇지 않으면 `/users/{user_id}`는 매개변수 `user_id`의 값을 `"me"`라고 생각하여 실행된다.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me/")
async def read_user_me():
  return {"user_id"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
  return {"user_id" : user_id}
```



### 사전 정의 값

---

> 만약 경로 매개변수를 받는 경로 동작이 있지만, 유효하고 미리 정의할 수 있는 경로 매개변수 값을 원한다면 파이썬의 Enum을 사용할 수 있다.

- Enum 클래스 생성

  - Enum을 임포트하고 str과 Enum을 상속하는 서브 클래스를 만듦
  - str을 상속함으로써 API문서는 값이 String 형이어야 하는 것을 알게되고 제대로 렌더링할 수 있게 됨
  - 고정값으로 사용할 수 있는 유효한 클래스 속성을 만듦

  ```python
  from enum import Enum
  from fastapi import FastAPI
  
  class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
  app = FastAPI()
  
  @app.get("/models{model_name}")
  async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
      return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
      return {"model_name": model_name, "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}
  ```




### 경로 매개변수 선언

---

- 생성한 열거형 클래스를 사용하는 타입 어노테이션으로 경로 매개변수를 만든다.

```python
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
  alextnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"
  
app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
  # enum 비교하기
  if model_name == ModelName.alexnet:
    return {"model_name": model_name, "message": "Depp Learning FTW!"}
  # enum 값 가져오기
  if model_name.value == "lenet":
    return {"model_name": model_name, "message": "LeCNN all the images"}
  # JSON 형식으로 return
  return {"model_name": model_name, "message": "Have someresiduals"}
```

- Swagger 확인 - 경로 매개변수에 사용할 수 있는 값이 선택되게 미리 정의되어 문서에 표시됨



### OpenAPI 지원

---

- 테스트와 정의가 어려워지는 OpenAPI는 경로를 포함하는 경로 매개변수를 내부에 선언하는 방법을 지원하지 않는다.
- 하지만, Stralette의 내부 도구 중 하나를 사용하여 FastAPI에서 사용 가능하다.



### 경로 변환기

---

- Starlett에서 옵션을 사용하면 다음과 같은 URL을 사용하여 path를 포함하는 경로 매개변수를 선언할 수 있다.

  `/files/{file_path:path}` : 이러한 매개변수의 이름은 file_path이고, 마지막 부분 `:path`는 매개변수가 경로와 일치해야함을 알려준다.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
  return {"file_path": file_path}
```

- 매개변수 : `/home/johndoe/myfile.txt` -> 이 경우 URL : `files//home/johndoe/myfile.txt`이고, files와 home 사이에 이중 슬래시 (//)가 생긴다.



### 쿼리 매개변수

---

- 경로 매개변수의 일부가 아닌 다른 함수 매개변수를 선언할 때, "쿼리" 매개변수로 자동 해석한다.

```python
from fastapi import FastAPI

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
  return fake_items_db[skip : skip + limit]
```

- 쿼리는 URL의 `?` 후에 나오고 `&`로 구분되는 키-값 쌍의 집합이다.
- `http://localhost:8000/items/?skip=0&limit=10`
- URL의 일부이기 때문에 자동으로 값은 문자열 취급이 된다. 하지만 파이썬 타입과 함께 선언 시, 해당 타입으로 변환되고 이를 검증한다.
- 만약 `http://localhost/items/`로 이동한 경우 -> 기본값으로 지정한 값인 `skip=0, limit=10`이 된다.



### 선택적 매개변수 - Optional[str] = None

---

- 쿼리 매개변수와 같은 방법으로 기본값을 None으로 설정하여 선택적 매개변수를 선언할 수 있다.

```python
from typing import Optional 
from fastapi import FastAPI

app = FastAPI()

# 이 경우 함수 매개변수 q는 선택적이며, 기본값은 None이 된다.
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
  if q:
    return {"item_id": item_id, "q": q}
  return {"item_id": item_id}
```

- FastAPI는 q가 None이므로 선택적이라는 것을 인지한다.



### 쿼리 매개변수 형변환

---

- `bool`형으로 선언할 수 있고, 아래처럼 변환이 가능하다.

```python
from typing import Optional
from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
  item = {"item_id": item_id}
  if q:
    item.update({"q": q})
  if not short:
    item.update(
      {"description": "This is an amazing item that has a long description"}
    )
  return item

# short의 값 중 참에 해당하는 것들 (1, True, true, on, yes)
```



### 여러 경로/쿼리 매개변수

---

- 여러 경로 매개변수와 쿼리 매겨변수를 동시에 선언할 수 있다.
- 특정 순서로 선언할 필요가 없으며, 매개변수들은 이름으로 감지된다.

```python
from typing import Optional
from fastapi import FastAPI
app = FastAPI()

# !
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
	user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
  item = {"item_id": item_id, "owner_id": user_id}
  if q:
    item.update({"q": q})
  if not short:
    item.update(
    	{"description": "This is an amazing itme that has a long description"}
     )
  return item
```



### 필수 쿼리 매개변수

---

- 매개변수를 필수적(Required)하게 만들기

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
  item = {"item_id": item_id, "needy": needy}
  return item
```

만약 필수 매개변수인 `needy`를 넣지 않으면 다음과 같은 오류가 발생
`"msg": "field required", "type": "value_error.missing"`



### 매개변수 종합

```python
from typing import Optional
from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_user_item(
	item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
  item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
  return item
```

- `needy`, 필수적인 `str`
- `skip`, 기본값이 0인 `int`
- `limit`, 선택적인 `int`



### Pydantic's BaseModel

---

```python
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# 속성 중 타입이 Optional로 지정되어 있으면 선택적이다.
class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None
    
app = FastAPI()

# 선언한 class를 사용하여 파라미터 정의하기
@app.post("/items")
async def create_item(item: Item):
  return item
```



### Use the model

---

-   함수 내에서 선언한 모델의 모든 속성에 접근할 수 있다.

```python
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
 	tax: Optional[float] = None
    
app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
  item_dict = item.dict()
  if item.tax:
    price_with_tax = item.price + item.tax
    item_dict.update({"price_with tax": price_with_tax})
  return item_dict
```



### RequestBody + Path Parameter

---

-   경로 파라미터와 requestbody를 같이 선언할 수 있다.
-   **kwargs : keyword argument - 키워드를 제공함

```python
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
  name: str
  descpription: Optional[str] = None
  price: float
  tax: Optional[float] = None
    
app = FastAPI()

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
  # 딕셔너리의 형태로 item.dict를 전달한다.
  return {"item_id": item_id, **item.dict()}
```



### Request body + path + query parameters

---

-   You can also declare body, path and query parameters, all at the same time.
-   FastAPI will recognize each of them and take the data from the correct place.

```python
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None
    
app = FastAPI()

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
  result = {"item_id", **item.dict()}
  if q:
    result.update({"q": q})
  return result
```

-   The function parameters will be recognized as follows:
    -   If the parameters is also declared in the path, it will be used as a path parameter.
    -   If the parameter is of a singular type(like `int, float, str, bool`) it will be interpreted as a query parameter.
    -   If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.

-   Eng
    1.   recognize : 알아보다
    2.   singular : 단수형, 단수형의
    3.   interpret: 해석하다.
    4.   declare : 선언하다.

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
