@: 자바 메모리 관라 - Stack & Heap

# 개요

- JAVA에서 메모리 관리가 어떻게 이루어지는지 알아보기 위함
- Stack, Heap 영역의 각 역할에 대해 알아봄

---

### Stack

- Heap 영역에 생성된 Object 타입 데이터의 참조값이 할당된다.
- 원시타입의 데이터가 값과 함께 할당된다. 
- 지역변수들은 Scope에 따른 Visibility를 가진다.
- 각 Thread는 자신만의 Stack을 가진다.

Stack에는 Heap 영역에서 생성된 Object 타입의 데이터들의 참조를 위한 값들이 할당된다. 또한, 원시타입(primitive types) - (byte, short, int, long, double, float, boolean, char) 타입의 데이터들이 할당된다. 이때 **원시타입의 데이터들에 대해서는 참조값을 저장하는 것이 아니라 실제 값은 Stack에 직접 저장**하게 된다.

Stack 영역에 있는 변수들은 visibility를 가진다. 이는 변수 Scope에 대한 개념으로, 전역변수가 아닌 지역변수가 foo()라는 함수 내에서 Stack에 할당된 경우, 해당 지역변수는 다른 함수에서 접근할 수 없다. 예를 들어, foo()라는 함수에서 bar() 함수를 호출하고 bar() 함수가 종료되는 경우, bar() 함수 내부에서 선언한 모든 지역변수들은 Stack에서 pop되어 사라진다.

Stack 메모리는 Thread에 각각 하나씩 할당된다. 즉, Thread 하나가 새롭게 생성되는 순간 해당 Thread를 위한 Stack도 함께 생성되며, 각 Thread의 Stack 영역에는 접근할 수 없다.

