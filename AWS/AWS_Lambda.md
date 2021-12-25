### 개요

---

-   



### lambda_handler(event, context) 함수 뜯어보기

---

```python
def lambda_handler(event, context):
  # TODO implement
  return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda!')
  }
```



-   `Parameter`
    -   `event`
        -   요청이 들어왔을 때 Event에 관련한 정보들을 담고 있다. 
        -   `json` 형식으로 전달되어 body에 접근할 수 있다. -> `dict` 이외의 타입은 `NoneType`이 될 수 있다.
    -   `context` 
        -   컨텍스트 정보를 담고 있다.
        -   호출 및 함수, 런타임 환경에 대한 정보를 제공하는 메서드와 속성들을 제공한다.