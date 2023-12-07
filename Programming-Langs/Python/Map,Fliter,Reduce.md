### Lambda

------

```python
sum = lambda a, b: a + b
sum(3, 4) # 7
```

- 익명 함수: 메모리를 아끼고 가독성을 향상시킴
    - 일반적인 함수는 객체를 만들고 재사용을 위해 함수명으로 함수의 로직을 메모리에 할당한다.
- 사용 이유:
    - 익명함수이기 때문에 한번 쓰고 다음 줄로 넘어가면 Heap Memory에서 사라짐

### Map

------

```python
# map(function, iterable_obj)

nums = [1, 2, 3]

result = list(map(lambda i: i ** 2, nums))

result # [1, 4, 9]
```

- Python의 내장함수로, 입력받은 Iterable한 자료형의 각 요소가 paramter로 전달받은 함수의 수행 결과를 묶어 Map Iterator 객체로 리턴함

### Filter

------

```python
# filter(function, iterable_obj)
list(filter(lambda x: x > 0, [1, 2, 3])
```

- parameter로 받은 iterable_obj의 요소를 하나씩 parameter로 받은 function에 입력하여 True를 리턴하는 요소만 리턴함

### Reduce

---

```python
from functools import reduce

reduce(lambda x, y: x + y, [1, 2, 3]) # ((1 + 2) + 3)
```



### 3항 연산자

------

```python
# if - else
if a > 10:
		print('a가 10보다 크다')
else:
		print('a가 10보다 작다')

# ternary operator
result = 'a가 10보다 크다' if a > 10 else 'a가 10보다 작다'
```