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

> "튜플은 타@입의 이름이 따로 지정되어 있지 않은 '지정된 데이터의 묶음'이다."	

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

```
#### 4.4.1 Array
```

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

```swift
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
> ###### - weak 속성을 사용하는 객체는 항상 Optional타입이어야 한다.
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
# Closure

> **클로저란 ?**
> 
> - 사용자의 **코드 안에서 전달되어 사용할 수 있는 로직을 가진** '중괄호'로 구분된 코드의 블럭이며, **일급 객체의 역할**을 할 수 있다.
> - **일급 객체는 전달 인자로 보낼 수 있고, 변수/상수 등으로 저장하거나 전달할 수 있으며, 함수의 반환 값이 될 수도 있다.**
> - **참조 타입**이다.
> - 함수는 클로저의 한 형태로, 이름이 있는 클로저이다.



#### 클로저의 표현방식

```Swift
{ (parameter) -> returnType in
	// Logic
}
```



### 예시 : Inline Closure

> 함수가 따로 정의된 형태가 아닌 인자로 들어가 있는 형태의 클로저

```Swift
let reverseNames = names.sorted(by: { (s1: String, s2: String) -> Bool in
                                    return s1 > s2 })
```



## 클로저의 축약

### 1. 타입 생략

> 클로저는 다양한 형태로의 축약이 가능하다
> 
> - 코드의 모호성을 피하기 위해 타입을 명시하는 것이 좋을 때도 있다.

```Swift
let reverseNames = names.sorted(by: { s1, s2 in return s1 > s2 })
```

### 2. 반환 타입 생략

> 반환 키워드를 생략할 수 있다.

```Swift
let reverseNames = names.sorted(by : { s1, s2 in s1 > s2 })
```

### 3. 파라미터명 생략

> 파라미터 명을 축약해서 사용할 수 있다
> 
> - 인자의 표기는 $0부터 순서대로

```Swift
let reversedNames = names.sorted(by : { $0 > $1 })
```

### 4.연산자 메소드

> 연산자를 사용할 수 있는 타입의 경우 연산자만 남길 수 있다.

```Swift
let reversedNames = names.sorted(by : > )
```



## 후행 클로저

> 인자로 클로저를 넣기에 길이가 너무 길다면 후행 클로저를 통해 함수의 뒤에 위치시킬 수 있다.

```Swift
let reversedNames = names.sorted() { $0 > $1 }
```

> 함수의 마지막 인자가 클로저이고, 후행 클로저를 사용하면 괄호"()"를 생략할 수 있다.

```Swift
let reversedNames = names.sorted { $0 > $1 }
let reversedNames = names.sorted { (s1: String, s2: String) -> Bool in 
                                 return s1 > s2 }
```



## Closure Capture

> 클로저는 특정 문맥의 상수나 변수의 값을 캡쳐할 수 있다.
> 
> 즉, 원본 값이 사라져도 클로저의 Body 안에서 그 값을 활용할 수 있다.

```swift
func makeIncrementer(forIncrement amount: Int) -> () -> Int {
		var runningTotal = 0
		func incrementer() -> Int {
			runningTotal += amount
			return runningTotal
		}
	return incrementer
}

let plusTen = makeIncrementer(forIncrement: 10)
let plusSeven = makeIncrementer(forIn)

// 함수가 각각 실행되어도 실제로는 변수 runningTotal과 amount가 캡쳐되어 그 변수를 공유하기 때문에 누적된 결과를 가진다.
plusedTen = plusTen() // 10
plusedTen2 = plusTen() // 20
// 다른 클로저이기 때문에 고유의 저장소에 runningTotal과 amount를 캡쳐해서 사용한다.
let plusSeven = plusSeven()	// 7
let plusSeven2 = plusSeven() // 14
```



## Escaping Closure

> 클로저가 함수의 인자로 전달되지만 함수 밖에서 실행되는 것을 Escape한다고 한다.
> 
> 이러한 경우 매개변수의 타입 앞에 **@escaping**이라는 키워드를 명시한다.
> 
> > 다음과 같은 경우 사용한다.
> 
> > - 비동기로 실행되는 경우
> 
> > - completionHandler로 사용되는 클로저의 경우

- 일반적인 지역변수가 함수 밖에서 살아있는 것은 전역변수를 함수에 가져와서 값을 주는 것과 다름이 없지만, **클로저의 Escaping은 하나의 함수가 마무리된 상태에서만 다른 함수가 실행되도록 함수를 작성할 수 있다는 점에서 유리**하다.

- 이를 활용해 함수 사이에 실행 순서를 정할 수 있다.

	  

	  

  - @escaping 예제

```Swift
var completionHandler: [() -> Void] = []
  
func someFunctionWithEscapingClosure(completionHandler: @escaping () -> Void) {
  completionHandlers.append(completionHandler)
}
// 위 함수에서 인자로 전달된 completionHandler는 함수가 끝나고 나중에 처리된다.
// 만약 함수가 끝나고 실행되는 클로저에 @escaping키워드를 붙이지 않으면 컴파일 시 오류가 발생한다.
  
// @escaping을 사용하는 클로저에서는 self를 명시적으로 언급해야 한다.
func someFunctionWithNoneescapingClosure(closure: () -> Void) {
  closure()	// 함수 안에서 끝나는 클로저
}
  
class SomeClass {
  var x = 10
  func doSomething() {
    someFunctionWithEscapingClosure { self.x = 100 } // 명시적으로 self를 적어줘야 한다.
    someFunctionWithNoneescapingClosure { x = 200 } 
  }
}
  
let instance = SomeClass()
instance.doSomething()
print(instance.x) // 200
  
completionHandlers.first?()
print(instance.x)	// 100
```

  

## AutoClosure

> 자동 클로저는 인자 값이 없으며, 특정 표현을 감싸서 다른 함수에 전달인자로 사용할 수 있는 클로저이다.
> 
> - 자동 클로저는 클로저를 실행하기 전까지 실행되지 않는다.
> - 즉, 실제 계산이 필요할 때 호출되기 때문에 계산이 복잡한 연산을 하는데 유용하다.

```Swift
var cunstomersInline = ["Chris", "Alex", "Ewa", "Barry", "Daniella"]
print(customerInline.count) // 5

let customerProvider = { customersInline.remove(at: 0) } // count가 줄어들지 않는다.
print(customersInline.count) // 5

// customerProvider가 실행되었을 때 동작한다.
print("Now serving \(customerProvider())!") // "Now serving Chris!"
print(customersInline.count) // 4
```



- 자동 클로저를 함수의 인자 값으로 넣는 예제

```Swift
func serve(customer customerProvider: () -> String) {
  print("Now serving \(customerProvider())!")
}
  
// Serve함수는 인자로 () -> String을 가진다.
// 이 함수에 클로저를 명시적으로 직접 넣을 수 있다.
serve(customer: { customerInline.remove(at: 0) } ) // "Now serving Alex!"
```

  

- @autoclosure 키워드를 붙임으로써 인자 값은 자동으로 클로저로 변환된다. (중괄호 생략 가능)
- 자동 클로저는 명시가 분명한 경우에만 사용하자.



- @autoclosure + @escaping

```Swift
var customersInline = ["Barry", "Daniella"]
var customerProviders: [() -> String] = []
  
 // 클로저를 인자로 받아 해당 클로저를 customerProviders 배열에 추가하는 함수 선언
func collectCustomerProviders(_ customerProvider: @autoclosure @escaping () -> String) {
  customerProviders.append(customerProvider)
}
  
collectCustomerProviders(customersInline.remove(at: 0)) // 클로저를 customerProviders 배열에 추가
collectCustomerProviders(customersInline.remove(at: 0))
  
print("Collected \(customerProviders.count) closures.")	// 2개의 클로저가 추가됨
  
for customerProvider in customerProviders {
  print("Now serving \(customerProvider())!") // 클로저를 실행하면 배열의 0번째 원소를 제거하며 그 값을 출력
}
// "Now serving Barry!"
// "Now serving Daniella!"
```

  

----

## Subscript

> - 컬렉션, 리스트, 시퀀스 등 집합의 특정 Member Elements에 간단히 접근할 수 있다.
> - 추가적인 메소드 없이 특정 값을 할당하거나 가져올 수 있따.
> - Ex.) Array[index]로 배열의 항목과 Dictionary[key]로 딕셔너리 항목에 접근하는 것



### 기본 형태

- 메소드와 연산 프로퍼티의 선언과 비슷하다.
- 하지만, 서브스크립트는 read-write와 read only만 가능하다.
- set에 대한 인자 값을 따로 지정하지 않으면 기본값으로 newValue가 지정된다.

```Swift
subscript(index: Int) -> Int {
	get {
    // 반환 값
 	}
	set(newValue) {
    // Set 액션
	}
}
```


- Read-Only로 선언하고 싶다면 아래와 같이 키워드를 따로 지정하지 않으면 get으로 동작한다.

```Swift
subscript(index: Int) -> Int {
  // return Get
}
```

- Read-Only 서브 스크립트 예시

  ```Swift
  struct TimesTable {
    let multiplier: Int
    subscript(index: Int) -> Int {
      return multiplier * index
    }
  }
  let threeTimesTable = TimesTable(multiplier: 3)
  print("six times three is \(threeTimesTable[6])")
  // "six times three is 18"
  ```

  

