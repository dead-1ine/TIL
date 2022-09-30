### FP의 정의
상태변화와 변경가능한 데이터는 가능한 피하면서 작성하는 프로그래밍

### FP의 장점
1. 명료함
2. 효율성
3. 테스트 용이성
4. 병렬처리

### FP의 핵심
#### 순수 함수(Pure Function)
- 출력은 매개변수에만 의존되며, 외부 상태에 상관없다.
- 사이드 이펙트가 없다. (외부 내용을 수정하지 않는다.)
- 입력이 같으면 출력도 같다.

### OOP vs FP
- OOP는 캡슐화를 통해 사이드 이펙트를 제어
- FP는 사이드 이펙트를 아예 배제
- FP는 No Object 변수를 최대한 지양

### 파이썬 FP 기능들
파이썬은 멀티패러다임 언어지만 FP를 위한 기능들이 존재한다.
- Map Reduce
- High order function
- Lambda
- Generator
- Iterator

#### High Order Function ==> 함수를 데이터처럼 사용함
```python
# 예제 1

def highFunc(f, a, b):
	return f(a, b)
def add(a, b):
	return a + b


# 예제 2

def make_add_func(add):
	def add(a):
		return a + add
	return add
# ex
add_func = make_add_func(10)
add_func(30)
make_add_func(10)(30)

```
- 이렇게 사용가능한 이유는? ==> 파이썬 함수는 1급 객체이다.
	- 장점은 구현을 미룰 수 있다.
	- 아직 구현되지 않은 기능이 있더라도 그것에 관한 Signiture만 있다면 함수를 받아서 조합해 사용할 수 있다.

#### Closure: 함수가 저장되는 데이터
```python
# 예제 3

value = 10
def func(a):
	value_copy = value
	def add(b):
		return value_copy + a + b
	return add

add_func = func(10)
value = 20
add_func(5) # 10 + 10 + 5
# 중간에 전역변수 value가 바뀌었지만 영향을 받지 않는다.
```

### 파이썬에서 FP 사용 시 문제점
- tail recursion optimization X
- Lambda의 불펺마
- immutable data를 직접 만들어야 함
- Curring이 안됨

#### tail recursion optimization 이슈
- 꼬리 재귀를 만들면 자동적으로 최적화시켜주는 언어가 있음(메모리 공간 최적화)
- 하지만 파이썬은 없다.
```python
def recursive(i):
	if(i == 1000):
		return print("Done")
	recursive(i + 1)
recursive(0)

RecursionError: maximum recursion depth exceeded while calling a Python object
```
- 파이썬의 Default Maximum Recursion Depth는 대략 1000임
- 옵션값 변경으로 제한을 풀기 전까지 원활하게 사용이 힘듦
- 왜 이런 현상이 발생하는가 ?
	- 파이썬은 순수 함수 지향형 언어가 아니기 때문이다. 그러므로 일일히 만들어야 한다.
- 해결책 ==> @Decorator(Syntactic Sugar)
```python
# 예제 4

# 꼬리재귀 최적화를 유도하는 함수
def tail_recursive(f):
	def decorated(*args, **kwargs):
		while True:
			try:
				return f(*args, **kwargs)
			except Recurse as r:
				args = r.args
				kwargs = r.kwrags
				continue
	return decorated

# 단점은 하나하나 만들기 어려움
```

#### Functional하게 문제를 해결하는 순서
1. 문제를 쪼갠다.
2. 쪼개진 문제를 더 쪼갠다.
3. 하나의 문제를 해결하는 순수함수를 만든다.
4. 순수함수를 결합한다.

#### 접근법에 대한 비교
- OOP : 객체를 만들고 객체들끼리 협력시키는 방법으로 프로그래밍
- FP : 쪼개고 모듈화함

#### Python FP의 단점
- 느리다.
	- Lazy Evaluation
	- Memoization
- 모든 함수가 순수할 수 없다.
	- 하스켈같은 함수지향 언어도 순수함수만 존재하는 것은 아니다.
- 배울 것이 많다.
	- 데코레이터의 사용법을 정확히 숙지하면 여러 응용이 가능해진다.

