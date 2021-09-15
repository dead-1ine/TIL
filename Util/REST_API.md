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