### Best Code 
---
```python
found = ((name, batches) for name in order
if (batches := get_batches(stock.get(name, 0), 8)))
print(next(found))
print(next(found))

# 출력
# ('나사못', 4)
# ('나비너트', 1)

```


### 기억해야 할 내용
---
- 대입식을 통해 컴프리헨션이나 제너레이터 식의 조건 부분에서 사용한 값을 같은 컴프리헨션이나 제너레이터의 다른 위치에서 재사용할 수 있다. 이를 통해 가독성과 성능을 향상시킬 수 있다.
- 조건이 아닌 부분에도 대입식을 사용할 수 있지만, 그런 형태의 사용은 피해야 한다.