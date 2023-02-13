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

enum을 사용할 때, 많은 경우 value가 무엇인지는 크게 중요하지 않다. 이럴 때는 enum 모듈의 auto() helper함수를 상요하면, 첫 번째 상수에 1, 두 번째 상수에 2, 이렇게 1씩 증가시키면서 모든 상수에 유일한 숫자를 값으로 할당한다.

```python
from enum import Enum, auto

class Skill(Enum):
    HTML = auto()
    CSS = auto()
    JS = auto()
```

`auto()` 함수를 사용하면 기존 상수에 어떤 숫자가 할당해놨었는지 구애받지 않고 새로운 상수를 추가할 수 있는 장점도 있다.

뿐만 아니라, `Enum` 클래스의 `_generate_next_value_()` 메서드를 override하면 숫자가 아닌 다른 값을 자동 할당할 수 있다. 예를 들어, 상수의 이름과 동일한 문자열을 상수의 값으로 자동 할당할 수 있다.

## 