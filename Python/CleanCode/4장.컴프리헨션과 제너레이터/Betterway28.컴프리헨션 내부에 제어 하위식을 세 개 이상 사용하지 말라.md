### Best Code 1
---
- 이 예제는 간단하고 읽기 쉽기 때문에 컴프리헨션에서 다중 루프를 사용하는 것이 타당한 예이다.
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

# 출력 : [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Best Code 2
---
```python
squared = [[x**2 for x in row] for row in matrix]
print(squared)

# 출력 : [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
```

### 기억해야 할 내용
---
- 컴프리헨션은 여러 수준의 루프를 지원하며 각 수준마다 여러 조건을 지원한다.
- 제어 하위 식이 세 개 이상인 컴프리헨션은 이해하기 매우 어려우므로 가능하면 피해야 한다.