### GIL 이란?

---

- 파이썬 인터프리터가 한 스레드만 하나의 바이트코드를 실행시킬 수 있도록 해주는 Lock이다.
- 하나의 스레드에 모든 자원을 허락하고, 그 후에는 Lock을 걸어 다른 스레드는 실행할 수 없게 막는다.
- GIL은 하나의 쓰레드에게 모든 자원의 점유를 허락한다.
- 인터프리터에 락을 거는 방식으로 다중 코어를 병행하여 사용하지 못하도록 한다.



### 파이썬의 성능이 느린 이유

---

- 파이썬은 인터프리터를 통해 코드를 해석한다.
- 파이썬 코드가 실행되기 위해서는 파이썬 인터프리터 프로그램이 먼저 메모리에 로드되어 있어야 한다는 뜻이다.



### 파이썬의 메모리 관리

---

- 파이썬은 객체의 생성과 소멸을 reference count를 통해서 관리한다.

- refcount란 객체가 가지고 있는 속성으로 자신을 몇 군데에서 참조하고 있는지에 대한 속성이다.

- 파이썬 인터프리터는 ref count를 검사해서 해당 객체의 메모리 회수를 결정한다.

- 파이썬의 메모리는 이렇게 자동으로 관리된다.

  

### 파이썬 GIL

---

파이썬에서 한 스크립트를 실행하면 2개의 쓰레드가 생긴다고 가정하자. 
2개의 쓰레드를 1개의 코어 시스템에서 돌리면 동시에 돌아가는 것처럼 보여도 사실은 CPU가 두 쓰레드를 번갈아 처리하는 것이다.
특정 시점에서는 언제나 CPU는 단 하나의 쓰레드만 처리한다.

그런데 멀티코어 CPU는 어떻게 될까? C와 같은 언어의 다중 코어라면 쓰레드가 여러 코어에서 동시에 돌아간다.
하지만 파이썬 GIL 하에서는 코어가 몇 개든 상관없이 특정 시점에서는 반드시 하나의 코어만 실행된다.

GIL은 이렇게 특정 시점에서 언제나 하나의 쓰레드만 실행하도록 만든 것이다. 
다시 말해 특정 시점에서 인터프리터를 사용하는 쓰레드는 언제나 1개라는 것이다.

이렇게 Interpreter에 MutextLock을 걸어 GIL이라는 이름이 붙여졌다.



### 파이썬의 GIL 채택 이유

---

#### 이유

1. 파이썬 코드는 인터프리터를 통해 실행된다.
2. 파이썬의 객체는 덩치가 크고 ref count를 통해 메모리 관리가 이루어진다.

위 두가지 사실로 인터프리터는 객체에 참조가 생기거나 해제될 때마다 refcound를 증감하게 된다.
쓰레드 간에 공유하는 객체가 있다면 객체를 참조하는 연산은 경쟁 상태가 되고 모든 객체에 대해서 참조가 증가 또는 감소될 때 Lock을 걸어야 한다는 의미가 된다. 

즉, 모든 객체가 크리티컬 섹션이 된다.

정수 변수 하나까지 객체로 다루는 파이썬에서는 이렇게 객체마다 Lock을 걸어야 하는 작업은 매우 비효율적이므로, 파이썬은 인터프리터를 Lock해버렸다.
쓰레드가 몇 개건 CPU 코어에 관계없이 인터프리터를 사용하는 쓰레드는 오직 1개로 만들었다. 

##### 

- ref count의 문제점은 여러 쓰레드가 동시에 객체의 ref count를 수정할 수 있으니 RaceCondition이 발생한다. 이 문제를 막으려면 refcount를 수정하려고 할 때마다 lock을 걸어야 하는데, 모든 객체에 lock을 걸어야 하는 것도 부담이고, 교착상태의 위험성도 있다.

- 따라서 이 문제를 해결하고자 단 하나의 Lock, 인터프리터를 통째로 Lock을 거는 방식을 사용한 것이다. 이 방식은 deadlock을 방지할 수 있고, 모든 변수에 Lock을 거는 것으로 인한 성능 저하는 없어지지만, 모든 CPU 위에서 올라가는 프로그램을 Single-Threaded로 만든다는 단점이 있다.



### CPython에서 GIL이 선택된 이유

---

CPython은 파이썬 구현체 중 가장 보편적으로 사용되는 구현체이다. 
GIL은 CPython 개발자가 파이썬 초기에 직면한 문제의 해결책이었다고 한다.

- Thread-safe하지 않은 기존 C라이브러리를 쉽게 사용할 수 있음
- GIL은 구현이 간단함
- 하나의 Lock -> 단일 쓰레드 프로그램 성능의 향상

