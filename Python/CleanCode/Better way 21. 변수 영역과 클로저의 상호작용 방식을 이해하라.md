### 예제 2
---
```python
def sort_priority2(numbers, group):
	found = False # 영역: 'sort_priority2'
	def helper(x):
		if x in group:
			found = True # 영역: 'helper' - 좋지않음
			return (0, x)
		return (1, x)
	numbers.sort(key=helper)
	return found
```

이 문제는 초보 파이썬 프로그래머를 종종 당황하게 만들기 때문에 영역 지정 버그(scoping bug)라고 부르기도 한다.
하지만 이 동작은 의도에 따른 결과이다.
의도는 함수에서 사용한 지역 변수가 그 함수를 포함하고 있는 모듈 영역을 더럽히지 못하게 막는 것이다.
이런 식으로 처리하지 않으면 함수 내에서 사용한 모든 대입문이 전역 모듈 영역에 쓰레기 변수를 추가하게 된다.
그 결과, 추가된 불필요한 변수들로 인해 잡음이 늘어날 뿐 아니라 추가된 전역 변수와 클러저의 상호작용에 의해 알아내기 힘든 미묘한 버그가 생길 수 있다.

파이썬에는 클로저 밖으로 데이터를 끌어내는 특별한 구문이 있다.
`nonlocal` 문이 지정된 변수에 대해서는 앞에서 설명한 영역 결정 규칙에 따라 대입될 변수의 영역이 결정된다. `nonlocal`의 유일한 한계점은 (전역 영역을 더럽히지 못하도록) 모듈 수준 영역까지 변수 이름을 찾아 올라가지 않는다는 것뿐이다.


- 다음은 같은 함수를 다시 정의하되 `nonloacl`을 사용한 코드다.
```python
def sort_priority2(numbers, group):
	found = False
	def helper(x):
		nonloacl found # 추가함
		if x in group:
			found = True
			return (0, x)
		return (1, x)
	numbers.sort(key=helper)
	return found
```

`nonlocal` 문은 대입할 데이터가 클로저 밖에 있어서 다른 영역에 속한다는 사실을 분명히 알려준다.
이 문장은 변수 대입 시 직접 모듈 영역(전역 영역)을 사용해야 한다고 지정하는 `global`문을 보완해준다.

하지만 전역 변수를 사용하는 여러 안티 패턴의 경우와 마찬가지로, 간단한 함수 외에는 어떤 경우라도 `nonlocal`을 사용하지 말라고 경고하고 싶다.
특히 함수가 길고 `nonlocal` 문이 지정한 변수와 대입이 이뤄지는 위치의 거리가 멀면 함수 동작을 이해하기 더 힘들어진다.

`nonlocal`을 사용하는 방식이 복잡해지면 도우미 함수로 상태를 감싸는 편이 더 낫다.
앞에서 본 `nonlocal` 을 사용하는 코드와 같은 결과를 달성하는 클래스를 정의해보자.
이 코드는 약간 길지만 읽기는 더 쉽다.

```
class Sorter:
	def __init__(self, group):
		self.group = group
		self.found = False

	def __call__(self, x):
		if x in self.group:
			self.found = True
			return (0, x)
		return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True
```

### 기억해야 할 내용
---
- 클로저 함수는 자신이 정의된 영역 외부에서 정의된 변수도 참조할 수 있다.
- 기본적으로 클로저 내부에 사용한 대입문은 클로저를 감싸는 영역에 영향을 끼칠 수 있다.
- 클로저가 자신을 감싸는 영역의 변수를 변경한다는 사실을 표시할 때는 `nonlocal`문을 사용하라.
- 간단한 함수가 아닌 경우에는 `nonlocal` 문을사용하지 말라.


