# Better way 25. 위치로만 인자를 지정하게 하거나 키워드로만 인자를 지정하게 해서 함수 호출을 명확하게 만들라

### 기억해야 할 내용
---
- 키워드로만 지정해야 하는 인자를 사용하면 호출하는 쪽에서 특정 인자를(위치를 사용하지 않고) 반드시 키워드를 사용해 호출하도록 강제할 수 있다. 이로 인해 함수 호출 의도를 명확히 할 수 있다. 키워드로만 지정해야 하는 인자는 인자 목록에서 * 다음에 위치한다.
- 위치로만 지정해야 하는 인자를 사용하면 호출하는 쪽에서 키워드를 사용해 인자를 지정하지 못하게 만들 수 있고, 이에 따라 함수 구현과 함수 호출 지점 사이의 결합을 줄일 수 있다. 위치로만 지정해야 하는 인자는 인자 목록에서 `/` 앞에 위치한다.
- 인자 목록에서 `/`와 `*` 사이에 있는 파라미터는 키워드를 사용해 전달해도 되고 위치를 기반으로 전달해도 된다. 이런 동작은 파이썬 함수 파라미터의 기본 동작이다.