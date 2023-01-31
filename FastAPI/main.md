# FastAPI

- 특징

    - 빠름: (Starlette와 Pydantic 덕에) Node.js 및 Go와 대등할 정도로 매우 높은 성능
    - 빠른 코드 작성
    - 적은 버그
    - 직관적임
    - 배우고 사용하기 쉬움
    - 코드가 짧아 유지보수에 편함
    - 견고함
    - 표준에 기반함

    - API 문서를 자동으로 만들어 줌
        - Swagger UI
        - ReDoc



- 설치 가이드

    - fastapi

        ```console
        pip install fastapi
        ```

    - uvicorn

        ```console
        pip install uvicorn
        ```

        

- main.py

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/hello/{name}')
async def say_hello(name: str):
    return {'message': f'Hello {name}'}
```



- 서버 실행

```console
uvicorn main:app --reload
```

- main: main.py 파일
- app: the object created inside of main.py with the line `app = FastAPI()`
- --reload: 코드가 변경된 후 자동으로 서버 재시작 (개발환경에서만 사용 권장)



### Open API 사용

- API를 빌드하는 동안 일반적으로 특정 행동을 수행하기 위해 특정 HTTP 메소드를 사용한다.
    - `POST`: 데이터를 생성하기 위해
    - `GET`: 데이터를 읽기 위해
    - `PUT`: 데이터를 업데이트하기 위해
    - `DELETE`: 데이터를 삭제하기 위해
- OpenAPI에서는 각 HTTP 메소드들을 '동작'이라 부른다.

- FastAPI에서 OpenAPI 규칙은 강제되는 것이 아니다. 다만 기능에 맞게 사용하는 것을 권장한다.'