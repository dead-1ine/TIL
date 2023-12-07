// 변수와 상수 
// 변수 선언은 var
// 상수 선언은 let
// var 변수명: type
// let 변수명: type

// 당연하게 선언과 동시에 값을 할당
var a: Int = 100


// Type Annotation
// 값을 통해 자동으로 타입을 지정한다.
var a = 100 

// 타입 확인 함수
type(of: a) // Integer.Type


// Bool Type
let a = true
let b = false

let c = !a // a의 부정으로 false가 됨


// # Numeric Type
let a: Int = 100
let b: Int64 = Int64(a)

let x: Double = 1.4
let y: Float = Float(x)


// # String Type
let result = 3 + 7
let s: String = "Result is \(result) 입니다."


// # Array<Element> Type
// 하나의 배열에 다른 타입이 섞여있으면 컴파일 에러를 발생시킴
let i = [1, 2, 3, 4, 5]
let s = ["a", "b", "c"]
let ia = [[1, 2], [3, 4]]
let x = [1, 2, "a"] // Error

var list = [1, 2, 3]
list[1] // 2
list[1] = 4
list // [1, 4, 3]
list.append(2) // [1, 4, 3, 2]
list.insert(0, at: 0) // [0, 1, 4, 3, 2]
list.remove(at: 2) // [0, 1, 3, 2]
list.removeAll // []


// # Dictionary<Key, Value> Type
let a = [1: "a", 2: "b", 3: "c"] // [Int: String]

// Dictionary Handling
let a = ["a": 1]
let b = a["a"] // 키에 해당하는 값이 나온다. 1

let dic = ["key1": "val1"]
let v1 = dic["key1"] != nil // true
let v2 = dic["key2"] != nil // false

// 변경
var a1 = ["key": 1]
a1["key"] = 3
a1 // ["key": 3]

// 추가
var a2 = ["key1": 1]
a2["key2"] = 2
a2 // ["key1": 1, "key2": 2]

// 삭제
var a3 = ["key": 1]
a3["key"] = nil
a3 // [:]


// # Optional<Wrapped> Type
// Swift 언어의 변수와 상수는 기본적으로 nil을 허용하지 않는다.

// Optional<Wrapped> Type은 Wrapped 타입의 값 여부에 따라 두 가지로 나뉜다.
enum Optional<Wrapped> {
    case none // 값이 없는 경우(nil)
    case some(Wrapped) // 값이 존재하는 경우
}

let n = Optional<Int>.none
print(".none: \(n)") // nil

let s = Optional<Int>.some(5)
print(".some: \(s)") // Optional(5)

// enum 케이스보다 더 간단하게 Optional을 생성하려면 아래와 같이 ?을 사용하면 된다.
var a: Int?

a = nil // nil 대입에 의한 .none 생성
a = Optional(5) // 이니셜라이저에 의한 .some 생성
a = 3 // 대입에 의한 .some 생성

// 단, nil 리터럴은 기본 타입이 정해지지 않았으므로 Type annotation을 우선적으로 해주어야 한다.
let a: Int? = nil
let b = nil // 타입이 결정되지 않은 상태이므로 컴파일 에러 발생

// 이니셜라이저로 전달된 인수를 기준으로 타입 추론이 이루어져 사용 가능
let a = Optional(10) // Optional<Int>
let b = Optional("abc") // Optional<String>

// Optional 타입은 값을 갖고 있지 않은 상태일 수 있어 고려해야 한다.
// Optional에서 값을 추출해내는 방법은 다음과 같다.
// - Optional Binding
// ??
// 강제로 풀기(Forced Unwrap)

// - Optional Binding
// 조건 분기문이나 반복문을 이용해 Optional 값의 유무에 따라 처리를 전환하는 방법
// Optional Binding은 if-let문을 이용해 처리한다.
let a = Optional("한")

if let r = a {
    // do something // a값이 존재하는 경우 실행됨
}

// - ??
// Optional 변수에 값이 없을 경우 기본값을 지정해줌
let a: Int? = 10
let b = a ?? 3 // a에 10이라는 값이 있으므로 b는 10이 대입됨

// 만약 값이 없다면 
let a: Int? = nil
let b = a ?? 3 // a는 nil이므로 3이 대입됨

// - Forced Unwrap
// ! 연산자에 의해 Optional Type에서 Wrapped타입의 값을 강제로 추출한다.
// 하지만 값의 존재를 명확히 알지 못한 상태에서 강제풀기를 진행하면 오류가 발생한다.
// 그러므로 권장하는 방법은 아님
let a: Int? = 10
let b: Int? = 3

a! + b! // 13

// Optional Chain은 Unwrap하지 않고 Wrapped 타입의 속성이나 함수에 접근하는 방식이다.
let a = Optional(10.0)
let b: Bool?

if let x = a { 
    b = x.isInfinite
} else {
    b = nil
}

print(b) // Optional(false)

// Wrapping하지 않고 Wrapped 타입의 속성이나 함수에 접근할 수도 있다.
let a = Optional(10.0)
let b = a?.isInfinite

print(b) // Optional(false)


// # Any Type
// Any Type은 모든 타입을 대입할 수 있다.
let s: Any = "한글"
let i: Any = 123123

// Any Type에 리터럴을 대입하면 원래 타입의 정보가 손실되어 기존 타입에서 가능했던 작업을 동일하게 진행하는 것이 불가능하다.
let a: Any = 1
let b: Any = 2

// 두 변수 다 Any이므로 서로 더할 수 없음
a + b // Compile Error


// # Tuple Type
// 여러 타입을 하나의 타입으로 모아 취급하는 것이 Tuple이다.
// Tuple의 요소가 되는 타입은 ()로 구분하여 열거하며 타입이나 갯수의 제한이 없다.
var t: (Int, String)
t = (1, "a")

var u: (Int, String, Double)
u = (1, "a", 12.3)

// Tuple의 요소에 접근하려면 Tuple을 정의할 때 요소 이름을 지정하면 된다.
let t = (int: 1, string: "a")
let i = t.int // 1
let s = t.string // "a"


// # Type Casting
// - 타입 판정
    // 값의 타입을 확인하려면 is 연산자를 사용하면 된다
let a: Any = 12
let b = a is Int // true

// - 상위 캐스팅
// 상위 캐스팅은 연산자 as를 사용한다.
let a = "abc" as Any // String 보다 Any가 상위 타입이므로 캐스팅 가능

// - 하위 캐스팅
let a = 12 as Any 
let b = a as? Int // Optional(12)
let x = a as? String // nil