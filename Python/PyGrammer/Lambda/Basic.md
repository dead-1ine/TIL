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







