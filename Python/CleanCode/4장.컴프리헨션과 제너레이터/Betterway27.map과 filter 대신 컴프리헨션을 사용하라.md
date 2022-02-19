### Worst Code
---
- map과 filter의 조합은 시각적인 잡음이 많다.
```python
alt_dict = dict(map(lambda x: (x, x**2),
					filter(lambda x: x % 2 == 0, a)))
alt_set = set(map(lambda x: x**3,
				  filter(lambda x: x % 3 == 0, a)))
```

### Best Code
---
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sqaures_dict = {x: x**2 for x in a if x % 2 == 0}
threes_cubed_set = {x**3 for x in a if x % 3 == 0}
print(even_squares_dict) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
print(threes_cubed_set) # {216, 726, 27}
```

### 기억해야 할 내용
---
- 리스트 컴프리헨션은 `lambda` 식을 사용하지 않기 때문에 같은 일을 하는 `map`과 `filter` 내장 함수를 사용하는 것보다 더 명확하다.
- 리스트 컴프리헨션을 사용하면 쉽게 입력 리스트의 원소를 건너뛸 수 있다. 하지만 `map`을 사용하는 경우에는 `filter`의 도움을 받아야만 한다.
- 딕셔너리와 집합도 컴프리헨션으로 생성할 수 있다.