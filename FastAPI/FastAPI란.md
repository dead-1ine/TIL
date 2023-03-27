### FastAPI란?

---

파이썬 웹 프레임워크 중 가장 유명한 Django와 Flask는 주로 웹 서비스를 만들 때 사용한다. 하지만 FastAPI는 API를 만드는 데 보다 집중한 프레임워크이다.

> Django나 Flask로 API를 만들지 못하는 것은 아니다. 다만, API를 작성하는 데에는 FastAPI가 좀 더 유리하다. Django에도 FastAPI와 비슷한 역할을 하는 DRF(Django REST Framework)가 있다.



### 속도가 빠르다.

---

FastAPI는 파이썬 웹 프레임워크 중 가장 빠르다고 알려졌다. NodeJS 및 Go와 대등할 정도로 높은 성능을 자랑한다. 이것이 가능한 이유는 FastAPI가 내부적으로 Starlette이라는 비동기 프레임워크를 사용하기 때문이다.

- Starlette: 비동기 ASGI 프레임워크(https://www.starlette.io/)



### 빠르게 작성할 수 있다.

---

API 개발은 보통 입출력 스펙을 정하고 기능을 구현한 후 테스트하는 순서로 진행한다. FastAPI는 입출력을 정의하고 입출력 값의 검증을 빠르고 안전하게 할 수 있다.(Pydantic의 기능) 그리고 작성한 API는 자동으로 생성되는 API 문서를 통해 손쉽게 테스트할 수 있다.(Swagger의 기능)

- Pydantic: 입출력 항목을 정의하고 검증(https://pydantic-docs.helpmanual.io/)
- Swagger: API 스펙 문서를 자동화(https://swagger.io/)



### 테스트 가능한 API 문서

---

FastAPI로 작성한 API는 API 사용법에 관한 문서를 자동으로 생성해주기 때문에 따로 작성할 필요가 없다. API 문서는 웹 페이지 형태로 제공되며 API 동작을 테스트할 수 있다.(Pybo의 기능)

- Pybo API Docs: http://fastapi.pybo.kr/docs



### Database

---

FastAPI는 Django처럼 자체 ORM(Object Relation Mapping)을 제공하지 않는다. 하지만 SQLAlchemy를 사용하여 ORM을 사용할 수 있다.(SQLAlchemy는 한번 익혀두면 두고두고 써먹을 수 있는 귀한 라이브러리)

- SQLAlchemy: Python에서 가장 많이 사용되는 ORM 라이브러리([https://www.sqlalchemy.org](https://www.sqlalchemy.org/))



### 견고한 API 공장

---

입출력 정의와 입출력 값을 검증하는 것이 패턴화되어 있어 견고하다는 인상을 준다. 그리고 정의된 입출력을 통해 API 문서가 자동으로 생성된다. 따라서 FastAPI는 API를 잘 만들어내는 훌륭한 공장과도 같다.