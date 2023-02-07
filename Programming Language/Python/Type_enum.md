# Python Enum Type

Python은 3.4버전부터 enum(enumeration) 타입을 지원한다. enum은 여러 개의 상수의 집합을 정의할 때 사용하며 enum 클래스를 사용하면 인스턴스의 종류를 제한할 수 있기 때문에 견고한 프로그램을 작성하는데 도움이 준다.



### 클래스 타입 정의

```python
from enum import Enum

class Skill(Enum):
    HTML = 1
    CSS = 2
    JS = 3
```

- enum 타입은 순회가 가능하기 때문에 `for`문으로 모든 상수를 쉽게 확인할 수 있다.

```python
for skill in Skill:
    print(skill)
```



### 값 자동 할당