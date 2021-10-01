### CORS(Cross Origin Resource Sharing)

---

-   CORS는 자바스크립트를 사용한 API 등의 리소스 호출 시 동일 출처(같은 호스트네임)가 아니더라도 정상적으로 사용 가능하도록 도와주는 방법



### Python Flask에서 CORS 설정

---

```python
pip install flask_cors

import flask_cors CORS, cross_origin

CORS(app) # 모든 도메인에 대한 CORS 설정
# CORS 에러가 더 이상 발생하지 않음
```



### 특정 주소, 도메인, 포트 등만을 사용 가능하도록 설정

---

-   모든 곳이 아닌 원하는 주소만 호출할 수 있도록 변경할 수 있다.
-   CORS( )의 두 번째 인자에 resources를 사용하고, origin과 그 값으로 허용할 도메인 주소를 입력한다.

```python
# 모든 곳에서의 호출을 허용
CORS(app, resources={r'*': {'origins': '*'}})
# 허용한 도메인 주소만 호출 허용
CORS(app, resources={r'*': {'origins': 'http://허용할 도메인 주소'}})
# 허용한 도메인 주소/_api/ 등의 주소를 호출할 때만 정상적으로 리소스를 전달
CORS(app, resources={r'/_api/*': 'http://허용할 도메인 주소'})
```



