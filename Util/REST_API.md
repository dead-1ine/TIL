# REST API

### fetch 사용법

---

>   -   fetch() 함수는 첫번째 인자로 URL, 두번째 인자로 options객체를 받고, Promise 타입의 객체를 반환한다.
>
>   -   반환된 객체는, API 호출이 성공했을 경우 response객체를 resolve하고, 실패했을 때는 error객체를 reject한다.

```javascript
fetch(url, options)
	.then((response) => console.log("response:", response))
	.then((error) => console.log("error:", error));
```

-   options 객체에는 HTTP 방식, HTTP 요청 헤더, HTTP 요청 전문(body)등을 설정해줄 수 있다.
-   response 객체로부터 HTTP 응답 상태(status), HTTP 응답 헤더(headers), HTTP 응답 전문(body) 등을 읽어올 수 있다.



### GET 호출

---

-   fetch() 함수는 디폴트로 GET 동작을 하고 GET 방식은 요청 전문을 받지 않기 때문에 옵션 인자가 필요없다.

    ```js
    fetch("https://jsonplaceholder.typicode.com/posts/1")
    	.then((response) => console.log(response)
    );
    
    # 결과
    Response {status: 200, ok: true, redirected: false, type: "cors", url: "https://jsonplaceholder.typicode.com/posts/1", …}
    ```

-   대부분의 REST API는 JSON 형태의 데이터로 응답하기 때문에, response 객체는 json() 메서드를 제공한다.

    ```js
    fetch("https://jsonplaceholder.typicode.com/posts/1")
    	.then((response) => response.json())
    	.then((data) => console.log(data));
    
    # 결과(JSON 객체 형태로 반환됨)
    {
      "userId": 1,
      "id": 1,
      "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
      "body": "quia et suscipit↵suscipit recusandae consequuntur …strum rerum est autem sunt rem eveniet architecto"
    }
    ```



### POST 호출

---

-   원격 API에서 관리하고 있는 데이터를 생성해야 한다면, 요청 전문을 포함할 수 있는 POST 방식의 HTTP 통신이 필요할 것이다.

    1.   위와 동일한 API를 대상으로 새로운 포스팅을 생성하기 위해 fetch() 함수를 사용한다.
    2.   method 옵션은 post로 지정해주고, headers 옵션을 통해 JSON 포맷을 사용한다고 알려줘야 함
    3.   요청 전문을 JSON 포맷으로 직렬화하여 가장 중요한 body 옵션에 설정해준다.

    ```js
    fetch("https://jsonplaceholder.typicode.com/posts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringfy({
        title: "Test",
        body: "I am testing!",
        userId: 1,
      }),
    }).then((response) => console.log(response));
    ```

    결과 : `Response {type: "cors", url: "https://jsonplaceholder.typicode.com/posts", redirected: false, status: 201, ok: true, …}`

    ```js
    fetch("https://jsonplaceholder.typicode.com/posts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: "Test",
        body: "I am testing!",
        userId: 1,
      }),
    })
      .then((response) => response.json())
      .then((data) => console.log(data));
    ```

    -   결과 : `{title: "Test", body: "I am testing!", userId: 1, id: 101}`



### PUT, DELETE 호출

---

-   PUT방식은 method 옵션만 PUT으로 설정한다는 점을 빼놓고는 POST 방식과 매우 흡사하다.

    ```js
    fetch("https://jsonplaceholder.typicode.com/posts/1", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: "Test",
        body: "I am testing!",
        userId: 1,
      }),
    })
      .then((response) => response.json())
      .then((data) => console.log(data));
    
    # 결과
    {title: "Test", body: "I am testing!", userId: 1, id: 1}
    ```

-   DELETE 방식에서는 보낼 데이터가 없기 때문에, headers와 body 옵션이 필요하지 않다.

    ```js
    fetch("https://jsonplaceholder.typicode.com/posts/1", {
      method: "DELETE",
    })
      .then((response) => response.json())
      .then((data) => console.log(data));
    
    # 결과
    {}
    ```

    

### [Bonus] 사용성 개선

---

>   `fetch()` 함수는 사용법이 아주 간단하지만, 계속 사용하다보면 똑같은 코드가 반복된다는 것을 느끼실 것입니다. 예를 들어, 응답 데이터을 얻기 위해서 `response.json()`을 매번 호출하거나, 데이터를 보낼 때, HTTP 요청 헤더에 `"Content-Type": "application/json"`로 설정해주는 부분은 지루하게 느껴질 수 있습니다. 뿐만 아니라, 기존에 사용하시던 라이브러리와 비교해봤을 때, `fetch()` 함수의 Promise 기반의 API가 좀 투박하다고 느끼실 수도 있습니다.

>   이럴 때는 `fetch()` 함수를 직접 사용하시기 보다는, 본인 입맛에 맞게 별도의 함수나 모듈로 빼서 사용하시기를 추천드립니다. 저같은 경우에는 프로젝트의 상황에 맞게 다음과 같이 async/await 키워드를 이용하여 HTTP 방식별로 비동기 함수를 작성하고 모듈화하여 사용하곤 합니다.

>   ```js
>   async function post(host, path, body, headers = {}) {
>     const url = `https://${host}/${path}`;
>     const options = {
>       method: "POST",
>       headers: {
>         "Content-Type": "application/json",
>         ...headers,
>       },
>       body: JSON.stringify(body),
>     };
>     const res = await fetch(url, options);
>     const data = await res.json();
>     if (res.ok) {
>       return data;
>     } else {
>       throw Error(data);
>     }
>   }
>   
>   post("jsonplaceholder.typicode.com", "posts", {
>     title: "Test",
>     body: "I am testing!",
>     userId: 1,
>   })
>     .then((data) => console.log(data))
>     .catch((error) => console.log(error));
>   ```



# { REST API } - Representational State Transfer API

---

### 탄생 배경

---

-   2000년도에 로이 필딩의 박사학위 논문에서 최초로 소개되었다.
-   로이 필딩은 HTTP의 주요 저자 중 한 명으로 그 당시 웹(HTTP) 설계의 우수성에 비해 제대로 사용되어 지지 않는 모습에 안타까워하며 웹의 장점을 최대한 활용할 수 있는 아키텍처로써 REST를 발표했다.

### REST 구성

---

1. Uniform Interface

    URI로 지정한 리소스에 대한 조작을 통일하고 한정된 인터페이스로 수행하는 아키텍처 스타일이다.

2. Stateless - 무상태성

    작업을 위한 상태정보를 따로 저장하거나 관리하지 않는다. 단순하게 클라이언트로부터 들어오는 요청만을 처리하면 됨. 이로 인해 서비스의 자유도가 높아지고 서버에 불필요한 정보를 관리하지 않음으로써 구현이 단순해진다.

3. Cacheable - 캐시 가능

    REST의 가장 큰 특징 중 하나는 HTTP 프로토콜을 그대로 사용하기 때문에 웹에서 사용하는 기존 기능들을 그대로 활용할 수 있다. 따라서 HTTP Caching 기능을 사용할 수 있고 구현이 가능하다.

4. Self-descriptiveness - 자체 표현 구조

    REST의 또 다른 큰 특징 중 하나는  REST API의 메세지만으로도 쉽게 이해할 수 있도록 구조화되어 있다.
    (Return 값으로 받은 데이터만으로도 요청의 성공유무와 데이터의 구조 등을 파악할 수 있다.)

5. Client - Server 구조

    REST 서버는 API만을 제공하고, 클라이언트는 사용자 인증이나 컨텍스트(세션, 로그인 정보) 등을 직접 관리하는 각각의 역할이 구분되는 구조를 통해 클라이언트와 서버에서의 개발해야할 내용이 분명히 나뉘어 서로의 의존서이 줄어든다.

6. 계층형 구조

    REST 서버는 다중 계층으로 구성될 수 있으며 보안, 로드 밸런싱, 암호화 계층을 추가해 구조를 유연하게 할 수 있다. 또한 Proxy, Gateway와 같은 네트워크 기반의 중간매체를 사용할 수 있다.



### REST API 디자인 가이드

---

REST API 설계 시 가장 중요한 항목은 2가지로 요약할 수 있다.

1.   URI는 정보의 자원을 표현해야 한다.
2.   자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다.



- URI는 정보의 자원을 표현해야 한다. (리소스명은 동사보다 명사를 사용할 것)

    `GET /members/delete/1`

    위와 같은 방식은 REST를 제대로 적용하지 않은 URI이다. URI는 자원을 표현하는데 중점을 두어야 한다. DELETE와 같은 행위에 대한 표현이 들어가서는 안된다.



- 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다.

    위의 잘못된 URI를 HTTP Method를 통해 수정해보면

    `DELETE /members/1`
    로 수정할 수 있다. 
    회원정보를 가져올 때는 GET, 회원 추가 시와 같은 표현을 할 때는 POST Method를 사용한다.