```python
lambda x: x + 10

plus_ten = lambda x: x + 10
plus_ten(1)
```



### 람다 표현식 자체를 호출

---

-   (lambda 매개변수들: 식)(인수)

```python
(lambda x: x + 10)(1) # 11
```



-   람다 표현식 안에서는 변수를 만들 수 없음

    ```python
    (lambda x: y = 10; x + y)(1)
    # SyntaxError: invalid syntax
    ```

    

-   람다 표현식 바깥에 있는 변수는 사용할 수 있음

    ```python
    y = 10
    (lambda x: x + y)(1) # 11
    ```

    

###  람다 표현식을 인수로 사용

---

>   람다 표현식을 사용하는 이유는 함수의 인수 부분에서 간단하게 함수를 만들기 위해서이다.
>
>   이런 방식의 대표적인 예는 map이다.

-   map() 사용하기

    ```python
    def plus_ten(x):
        return x + 10
    list(map(plus_ten, [1, 2, 3])) # [11, 12, 13]
    ```

-   Lambda로 변환

    ```python
    list(map(lambda x: x + 10, [1, 2, 3])) # [11, 12, 13]
    ```

    

### 람다 표현식에 조건부 표현 사용하기

---

-   lambda 매개변수: 식1 if 조건식 else 식2

    ```python
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list(map(lambda x: str(x) if x % 3 == 0 else x, a))
    # [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]
    
    # 조건식을 활용해 정수 3과 나누어 떨어지는 값을 str()한다.
    ```

    

-   lambda 표현식에서는 if를 사용했다면 반드시 else를 사용해야 한다.

    ```python
    list(map(lambda x: str(x) if x % 3 == 0, a))
    # SyntaxError: invalid syntax
    ```

-   lambda 표현식에서는 elif를 사용할 수 없다.

    ```python
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
    ```

-   억지로 람다를 사용하여 못 알아보는 경우가 생기지 않게 하자. 코드는 쉽게 작성하는 것이 좋다.

