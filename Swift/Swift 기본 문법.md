TODO - 문법의 기본적인 것들을 정리하며 복습하는 시간을 가짐

---- Swift의 메모리
Struct 타입은 value, Class 타입은 Reference.
Value는 Stack에 값을 저장하고, 변수에 대입 시 값을 복사함
Reference는 Stack에 주소를 저장하고 값을 Heap에 저장함
고로, 변수에 대입하면 Stack의 주소값이 대입되어 
같은 Heap을 가리키게 됨

---- 
### 메모리를 참조하는 방법(strong, weak, unowned)
> - ARC(Automatic Reference Counting)이란?
> - 컴파일 시 코드를 분석하여 자동으로 retain, release 코드를 생성
> - 참조된 횟수를 추적하여 더 이상 참조되지 않는 인스턴스를 메모리에서 해제
> - ARC는 자동으로 RC를 관리해주기 때문에 메모리 해제에 대한 개발자의 부담을 줄여준다.

#### strong (강한 참조)
> - 해당 인스턴스의 소유권을 가진다.
> - 자신이 참조하는 인스턴스의 retain count를 증가시킨다.
> - 값이 지정된 시점에 retain 되고 참조가 종료되는 시점에 release 된다.
> - 선언 시 아무것도 적지 않으면 default로 strong이 된다.
> ```swift
> var test = Test()	// retain Count 1 증가
> test = nil 	// retain count 1 감소, 메모리 해제
> ```
  
#### weak(약한 참조)
> - 해당 인스턴스의 소유권을 가지지 않고, 주소값만을 가지고 있는 포인터 개념이다.
> - 자신이 참조하는 인스턴스의 retain count를 증가시키지 않는다. release도 발생하지 않음
> - 자신이 참조는 하지만 weak 메모리를 해제시킬 수 있는 권한은 다른 클래스에 있다.
> - 메모리가 해제될 경우 자동으로 reference가 _nil로 초기화된다._
> - _weak 속성을 사용하는 객체는 항상 Optional타입이어야 한다._
> ```swift
> weak var test = Test()	// 객체가 생성되지만 weak이기 때문에 바로 객체가 해제되어 nil이 됨
> ```

#### unowned (미소유 참조 / 약한 참조)
> - 해당 인스턴스의 소유권을 가지지 않는다.
> - 자신이 참조하는 인스턴스의 retain count를 증가시키지 않는다.
> - nil이 될 수 없다. Optional로 선언되어서는 안된다.
> ```swift
> unowned var test = Test()	// 객체 생성과 동시에 해제되고 댕글링 포인트만 가지고 있음. 에러.
> ```

##### weak와 unowned의 차이
> - weak는 객체를 계속 추적하며 객체가 사라질 때 nil로 바꾼다.
> - 하지만, unowned는 객체가 사라지게 되면 댕글링 포인터가 남는다.
> - 이 댕글링 포인터를 참조하게 되면 crash가 발생하는데, 이 때문에 unowned는 사라지지 않을거라고 보장되는 객체에서만 사용해야 한다.
> - 댕글링 포인터(Dangling Pointer) : 원래 바라보던 객체가 해제되며 할당되지 않는 공간을 바라보는 포인터
---- 





