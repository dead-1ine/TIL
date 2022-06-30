# Python - Lambda



## Syntax

```python
lambda arguments : expression
```



- Add 10 to argument a, and return the result:

```python
x = lambda a: a + 10
print(x(5)) # 15
```



- Multiply argument a with argument b and return the result:

```python
x = lambda a, b: a * b
print(x(5, 6)) # 30
```



- Summarize argument a, b and c and return the result:

```python
x = lambda a, b, c: a + b + c
print(x(5, 6, 2)) # 13
```



## Use with map()

- map 함수는 `입력 함수`를 `입력 리스트`의 `item`에 적용하는 함수이다.
- 리스트의 데이터 형태를 변경할 때 자주 사용하는 함수이다.

```python
map(입력 함수, 입력 리스트)
```

```python
result = list(map(lambda x: x + 1, [1,2,3]))
result # [2, 3, 4]
```



## Use with filter()

- `filter` 함수는 입력리스트의 `item`에 입력 함수를 적용하고 참을 반환한다.

```python
filter(입력 함수, 입력 리스트)
```

```python
result = list(filter(lambda x: x > 5, [1, 2, 3, 4, 5, 6]))
result # 6
```



## Use with reduce()

- `reduce`함수는 리스트의 첫번째, 두번째 `item`을 인자로 받아 하나의 값을 반환하는 함수이다.

```python
reduce(입력 함수, 입력 리스트)
```

```python
from function import reduce

result = reduce(lambda x, y: x + y, [1, 2, 3])
result # 6
```



