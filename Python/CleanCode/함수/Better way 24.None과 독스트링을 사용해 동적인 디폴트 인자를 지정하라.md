```python
from typing import Optional

def log_typed(message: str,
			  when: Optional[datetime]=None) -> None:
	"""메시지와 타임스탬프를 로그에 남긴다.

	Args:
		message: 출력할 메시지
		when: 메시지가 발생한 시각(datetime)
			디폴트 값은 현재 시간이다.
	"""
	if when is None:
		when = datatime.now()
	print(f"{when}: {message}")
```

### 기억해야 할 내용
---
- 디폴트 인자 값은 그 인자가 포함된 함수 정의가 속한 모듈이 로드되는 시점에 단 한 번만 평가된다. 이로 인해 동적인 값({}, [], datetime.now() 등)의 경우 예기치 못한 동작이 일어날 수 있다.
- 동적인 값을 가질 수 있는 키워드 인자의 디폴트 값을 표현할 때는 `None`을 사용하라. 그리고 함수의 독스트링에 실제 동적ㅇ니 디폴트 인자가 어떻게 동작하는지 문서화해두라.
- 타입 애너테이션을 사용할 때도 `None`을 사용해 키워드 인자의 디폴트 값을 표현하는 방식을 적용할 수 있다.