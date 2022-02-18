### Best Code
---
```Python
from functools import wraps

def trace(func):
	@wraps(func)
	def wrapper(*args, **kwars):
		...
	return wrapper

@trace
def fibonacci(n):
	...
```


### 기억해야 할 내용
---
- 파이썬 데코레이터는 실행 시점에 함수가 다른 함수를 변경할 수 있게 해주는 구문이다.
- 데코레이터를 사용하면 디버거 등 인트로스펙션을 사용하는 도구가 잘못 작동할 수 있다.
- 직접 데코레이터를 구현할 때 인트로스펙션에서 문제가 생기지 않길 바란다면 `functools` 내장 모듈의 `wraps` 데코레이터를 사용하라.