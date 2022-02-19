> `concurrent.futures` 모듈은 비동기적으로 콜러블을 실행하는 고수준 인터페이스를 제공한다.

> 비동기 실행은 스레드(ThreadPoolExecutor)나 별도의 프로세스(ProcessPoolExecutor)로 수행할 수 있다. 둘 다 추상 클래스 Executor로 정의된 것과 같은 인터페이스를 구현한다.

### Executor 객체
---
`class concurrent.futures.Executor`
- 비동기적으로 호출을 실행하는 메서드를 제공하는 추상 클래스이다.
- 직접 사용해서는 안되며, 구체적인 하위 클래스를 통해 사용해야 한다.

`submit(fn, /, *args, **kwargs)`
- Schedules the callable, fn, to be executed as fn(*args, *kwargs) and returns a Future object representing the execution of the callable.
```python
with ThreadPoolExecutor(max_workers=1) as executor:
	future = executor.submit(pow, 323, 1235)
	print(future.result())
```

`map(func, *iterables, timeout=None, chunksize=1)`
- `map(func, *iterables)`와 비슷하지만 다음과 같은 차이가 있다.
	- `iterables`는 느긋하게 처리되는 것이 아니라 즉시 수집된다.
	- `func`는 비동기적으로 실행되며 `func`에 대한 여러 호출이 동시에 이뤄질 수 있다.

	반환된 이터레이터는 `__next__()`가 호출되었을 때, `Executor.map()`에 대한 최초 호출에서 `timeout` 초 후에도 결고를 사용할 수 없는 경우`concurrent.futures.TimeoutError` 를 발생시킨다.
	`timeout`은 `int` 또는 `float`가 될 수 있다. `timeout`이 지정되지 않았거나 `None`인 경우, 대기 시간에는 제한이 없다.

	`func`호출이 예외를 일으키면, 값을 이터레이터에서 꺼낼 때 해당 예외가 발생한다.

	`ProcessPoolExecutor`를 사용할 때, 이 메서드는 `iterables`를 다수의 덩어리로 잘라서 별도의 작업으로 풀에 제출한다. 이러한 덩어리의 크기(대략적인)는 `chunksize` 를 양의 정수로 설정하여 지정할 수 있다. 매우 긴 이터리블의 경우 `chunksize`에 큰 값을 사용하면 기본 크기인 1에 비해 성능이 크게 향상될 수 있다. `ThreadPoolExecutor`의 경우, `chunksize`는 아무런 효과가 없다.

