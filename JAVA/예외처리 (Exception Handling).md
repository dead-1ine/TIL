
- 컴파일 에러 : 컴파일 시에 발생하는 에러
- 런타임 에러 : 실행 시에 발생하는 에러
- 논리적 에러 : 실행은 되지만, 의도와 다르게 동작하는 것

>  자바에서는 실행 시(runtime) 발생할 수 있는 프로그램 오류를 ‘에러’와 ‘예외’, 두 가지로 구분한다.
> > - 에러 : 프로그램 코드에 의해서 수습될 수 없는 심각한 오류
> > - 예외 : 프로그램 코드에 의해서 수습될 수 있는 다소 미약한 오류

##### printStackTrace()와 getMessage()
> - 예외가 발생했을 때 생성되는 예외 클래스의 인스턴스에는 발생한 예외에 대한 정보가 담겨 있다.
> - catch블럭의 괄호에 선언된 참조 변수를 통해 이 인스턴스에 접근할 수 있다.

- printStackTrace() : 예외발생 당시의 호출스택(Call Stack)에 있었던 메서드의 정보와 예외 메시지를 화면에 출력한다.
- getMessage() : 발생한 예외클래스의 인스턴스에 저장된 메시지를 얻을 수 있다.

	```java
	try {
		System.out.println(0/0);	// 예외 발생
		System.out.println(4);		// 실행되지 않는다.
	} catch (ArithmetiecException ae) {
		ae.printStackTrace();
		// 참조변수 ae를 통해, 생성된 ArithmeticException인스턴스에 접근할 수 있다.
		System.out.println("예외 메시지 : " + ae.getMessage());
	}
	```


##### 예외 발생시키기
> 키워드 ‘throw’를 사용해 고의로 예외를 발생시킬 수 있다.
> > 방법 : 
> > > 1. 연산자 new를 이용해 발생시키려는 예외 클래스의 객체를 만든 다음 
> > > > ```java
> > > > Exception e = new Exception("고의로 발생시킴");
> > > > ```
> > > 2. 키워드 throw를 이용해서 예외를 발생시킨다.
> > > > ```java
> > > > throw e
> > > > ```

> 예시 
> ```java
> try {
> 	Exception e = new Exception("고의 발생");
> 	throw e; 	// 예외를 발생시킴
> //	throw new Exception("고의 발생");
> 	throw new Exception();
> 	throw new RuntimeException();
> }
> ```

##### 메서드에 예외 선언하기
```java
void method() throws Exception1, Exception2, ... ExceptionN {
	// 메서드 내용
}
```
