> ### 함수를 간단한 ‘식(expression)’으로 표현하는 방법
>
> ```java
> int max(int a, int b) {
> 	return a > b ? a : b
> }
> 
> // lambda
> (a, b) -> a > b ? a : b
> ```

> ### 함수와 메서드의 차이
>
> - 근본적으로 동일. 함수는 일반적 용어, 메서드는 객체지향개념 용어
> - 함수는 클래스에 독립적, 메서드는 클래스에 종속적

> ### 람다식 작성법
>
> 1. 메서드의 이름과 반환타입 제거 ‘-\>’를 블록 {} 앞에 추가
> 2. 반환값이 있는 경우, 식이나 값만 적고 return문 생략 가능
> 3. 매개변수의 타입이 추론 가능하면 생략가능(대부분 가능)

> ### 람다식 작성 주의사항
>
> 1. 매개변수가 하나인 경우, 괄호() 생략가능
> 2. 블록 안의 문장이 하나뿐일 때, 괄호{} 생략가능



> ### 람다식은 익명함수? 익명객체!
>
> 1. 람다식은 익명함수가 아니라 익명 객체이다.
> ```java
> (a, b) -> a > b ? a : b
> 
> new Object() {
> 	int max(int a, int b) {
> 		return a > b ? a : b;
> 	}
> }
> ```
> 람다식을 다루기 위한 참조변수가 필요.



### 함수형 인터페이스
> 함수형 인터페이스 - 단 하나의 추상 메서드만 선언된 인터페이스(Single Abstract Method)
> 람다식을 다루기 위해 사용
> ```java
> interface MyFunction {
> 	public abstract int max(int a, int b);
> }
> 
> MyFunction f = new MyFunction() {
> 	public int max(int a, int b) {
> 		return a > b ? a : b;
> 	}
> }
> 
> int value = f.max(3, 5) // OK.
> ```

> 함수형 인터페이스 타입의 참조변수로 람다식을 참조할 수 있음
> ```java
> MyFunction f = (a, b) -> a > b ? a : b;
> int value = f.max(3, 5);	// 실제로는 람다식이 호출됨
> 
> // 함수형 인터페이스와 람다표현식
> FunctionInterface functionalInterface = new FunctionalInterface() {
> 	@Override
> 	public void doSomething() {
> 		Sout("Do Something");
> 	}
> };
> 
> FunctionalInterface fi = () -> System.out.println("Do Something");
> ```

> @FunctionalInterface 어노테이션의 활용
> ```java
> // 만약 함수형 인터페이스가 아닌 경우, 컴파일 에러가 발생함(안전한 코딩을 위함)
> @FunctionalInterface
> public interface FuncInterface {
> 	void doSomething();
> }
> ```





