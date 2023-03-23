### FastAPI란?

---

파이썬 웹 프레임워크 중 가장 유명한 Django와 Flask는 주로 웹 서비스를 만들 때 사용한다. 하지만 FastAPI는 API를 만드는 데 보다 집중한 프레임워크이다.

> Django나 Flask로 API를 만들지 못하는 것은 아니다. 다만, API를 작성하는 데에는 FastAPI가 좀 더 유리하다. Django에도 FastAPI와 비슷한 역할을 하는 DRF(Django REST Framework)가 있다.



### 속도가 빠르다.

---

FastAPI는 파이썬 웹 프레임워크 중 가장 빠르다고 알려졌다. NodeJS 및 Go와 대등할 정도로 높은 성능을 자랑한다. 이것이 가능한 이유는 FastAPI가 내부적으로 Starlette이라는 비동기 프레임워크를 사용하기 때문이다.

- Starlette: 비동기 ASGI 프레임워크(https://www.starlette.io/)