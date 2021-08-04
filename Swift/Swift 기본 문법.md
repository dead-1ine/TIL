TODO - 문법의 기본적인 것들을 정리하며 복습하는 시간을 가짐

----

#### Swift의 메모리
Struct 타입은 value, Class 타입은 Reference.
Value는 Stack에 값을 저장하고, 변수에 대입 시 값을 복사함
Reference는 Stack에 주소를 저장하고 값을 Heap에 저장함
고로, 변수에 대입하면 Stack의 주소값이 대입되어 
같은 Heap을 가리키게 됨

----

### 데이터 타입 고급

- 스위프트의 특징 중 하나는 안정성(Safe)이 가장 뚜렷한 것이다
- 스위프트는 타입에 민감하며 엄격하다.
- 서로 다른 타입끼리의 데이터 교환은 타입캐스팅(Type-Casting)을 거쳐야 한다.
- 스위프트에서의 데이터 교환은 엄밀히 말하면 타입 캐스팅이 아닌 새로운 인스턴스를 생성하여 할당하는 것이다.

### 타입 추론

- 스위프트에서는 변수나 상수를 선언할 때 특정 타입을 명시하지 않아도 컴파일러가 할당된 값을 기준으로 타입을 결정한다.

  ```Swift
  // 타입을 지정하지 않았으나 타입 추론을 통해 name은 String 타입으로 선언된다.
  var name = "Test"
  ```

### 타입의 별칭

- 스위프트는 기본으로 제공하는 데이터 타입이나, 사용자가 임의로 만든 데이터 타입 등 이미 존재하는 데이터 타입에 임의의 다른 이름을 부여할 수 있다.

- 그 후 기본 타입과 이후 추가한 별칭을 모두 사용할 수 있다.

  ```swift
  typealias MyInt = Int
  typealias YourInt = Int
  typealias MyDouble = Double
  
  let age: MyInt = 100		// MyInt는 Int의 또 다른 이름이다.
  var year: YourInt = 2080	// YourInt도 Int의 또 다른 이름이다.
  
  // MyInt도, YourInt도 Int이기 때문에 같은 타입으로 취급합니다.
  year = age
  
  let month: Int = 7		// 물론 기존 Int도 사용 가능
  let percentage: MyDouble = 99.9		// Int 외의 다른 자료형도 모두 별칭 사용 가능
  ```

----

### 4.3 튜플

> "튜플은 타입의 이름이 따로 지정되어 있지 않은 '지정된 데이터의 묶음'이다."	

```swift
// String, Int, Double 타입을 갖는 튜플
var person: (String, Int, Double) = ("Yang", 100, 180)

// 인덱스를 통해 값을 뺄 수 있다.
print("이름: \(person.0), 나이: \(person.1), 신장: \(person.2)")

// 인덱스를 통해 값을 할당할 수 있다.
person.1 = 99
person.2 = 170

print("이름: \(person.0), 나이: \(person.1), 신장: \(person.2)")
```



- 튜플의 각 요소를 이름 대신 숫자로 표현하기 때문에 간편해 보일 수 있지만, 차후 다른 프로그래머가 볼 때 각 요소가 어떤 의미가 있는지 유추하기 어렵다. 
- 튜플의 요소마다 이름을 붙일 수 있다.

```swift
// String, Int, Double 타입을 갖는 튜플
var person: (name: String, age: Int, height: Double) = ("yang", 100, 180)

// 요소 이름을 통해 값을 뺄 수 있다
print("이름: \(person.name), 나이: \(person.age), 신장: \(person.height)")

person.age = 99		// 요소 이름을 통해 값을 할당
person.2 = 170		// 인덱스를 통해 값을 할당

// 기존처럼 인덱스를 이용하여 값을 뺄 수 있다.
print("이름: \(person.0), 나이: \(person.1), 신장: \(person.2)")
```



- typealias - Tuple : 타입 별칭을 통해 더 깔끔하고 안전하게 코드 작성

  ```swift
  typealias PersonTuple = (name: String, age: Int, height: Double)
  
  let yang: PersonTuple = ("yang", 100, 180)
  let eric: PersonTuple = ("Eric", 120, 182)
  
  print("이름: \(yang.name), 나이: \(yang.age), 신장: \(yang.height)")
  ```

----

# 컬렉션형

> 스위프트에는 Array, Dictionary, Set 등이 있다.

	#### 4.4.1 Array

> 배열은 같은 타입의 데이터를 일렬로 나열한 후 순서대로 저장하는 형태의 컬렉션 타입이다.

```swift
// 대괄호를 사용하여 배열임을 표현
var names: Array<String> = ["Yang", "test", "admin", "root"]

// 위 선언과 정확히 동일한 표현. [String]은 Array<String>의 축약 표현입니다.
var names: [String] = ["Yang", "test", "admin", "root"]

var emptyArray: [Any] = [Any]()	// Any 데이터를 요소로 갖는 빈 배열을 생성
var emptyArray: [Any] = Array<Any>()	// 위 선언과 정확히 같은 동작

// 배열의 타입을 정확히 명시했다면 []만으로도 빈 배열을 생성할 수 있다.
var emptyArray: [Any] = []
print(emptyArray.isEmpty) // true
print(names.count)	// 4
```



- 배열의 사용

  ``` swift
  print(names[2])	// admin
  names[2] = "jenny"
  print(names[2])	// jenny
  print(names[4]) // 오류! 인덱스의 범위를 벗어남
  
  names[4] = "elsa"	// 오류! 인덱스의 범위를 벗어남
  names.append("elsa")	// 마지막에 elsa가 추가됨
  names.append(contentsOf: ["john", "max"]) 		// 맨 마지막에 john과 max가 추가됨
  names.insert("happy", at: 2)	// 인덱스 2에 삽입됨
  // 인덱스 5의 위치에 jihee, minsoo가 삽입됨
  names.insert(contentsOf: ["jihee", "minsoo"], at: 5)
  
  print(names.index(of: "yang")) // 0
  print(names.index(of: "christal")) // nil
  print(names.first)	// yang
  print(names.last) // max
  
  let firstItem: String = names.removeFirst()
  let lastItem: String = names.removeLast()
  let indexZeroItem: String = names.remove(at: 0)
  
  print(firstItem)	// yang
  print(lastItem)	// max
  print(indexZeroItem)	// chulsoo
  print(names[1 ... 3]) // ["jenny", "yang", "jihee"]
  ```

  

----

## 메모리를 참조하는 방법(strong, weak, unowned)

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

##### 언제 쓰는가
- strong : reference count를 증가시켜 ARC로 인한 메모리 해제를 피하고, 객체를 안전하게 사용하고자 할 때 쓰인다. 
- weak : 대표적으로 retain cycle에 의해 메모리가 누수되는 문제를 막기 위해 사용한다. delegate 패턴이 있다.
- unowned : 객체의 라이프사이클이 명확하고 개발자에 의한 제어 가능이 명확한 경우, weak Optional 타입 대신 사용하여 보다 간결한 코딩이 가능하다.                                               
----
#### Closure Capture
> 클로저 캡처란 클로저가 매개변수나 지역변수가 아닌 외부의 Context를 사용하기 위해 주변 Context를 참조하는 것(Capturing by reference)입니다.
> 클로저는 정의된 Context 내의 상수나 변수에 대한 참조를 캡처하고 저장할 수 있다.

```swift
func makeIncrementer(forIncrement amount: Int) -> () -> Int {
		var runningTotal = 0
		func incrementer() -> Int {
			runningTotal += amount
			return runningTotal
		}
	return incrementer
}
```





