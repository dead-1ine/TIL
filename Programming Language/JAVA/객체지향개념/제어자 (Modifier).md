
##### static - 클래스의, 공통적인

대상 : 멤버변수, 메서드, 초기화 블럭

static이 붙은 멤버변수와 메서드, 그리고 초기화 블럭은 _인스턴스가 아닌 클래스에 관계된 것_이기 때문에 인스턴스를 생성하지 않고도 사용할 수 있다.

```java
class StaticTest {
	static int width = 200;		// 클래스 변수(static 변수)
	static int height = 120;	// 클래스 변수(static 변수)

	static {	// 클래스 초기화 블럭
		// static변수의 복잡한 초기화 수행
	}

	static int max(int a, int b) {	// 클래스 메서드(static 메서드)
		return a > b ? a : b;
	}	
}
```

##### final - 마지막의, 변경될 수 없는

대상 : 클래스, 메서드, 멤버변수, 지역변수

- 변수에 사용되면 값을 변경할 수 없는 상수가 된다.
- 메서드에 사용되면 오버라이딩을 할 수 없게 된다.
- 클래스에 사용되면 자신을 확장하는 자손클래스를 정의하지 못한다.

```java
final class FinalTest {		// 조상이 될 수 없는 클래스
	final int MAX_SIZE = 10;	// 값을 변경할 수 없는 멤버변수
	
	final void getMaxSize() {	// 오버라이딩할 수 없는 메서드
		final int LV = MAX_SIZE;// 값을 변경할 수 없는 지역변수
		return MAX_SIZE;
	}
}
```


##### abstract - 추상의, 미완성의

대상 : 클래스, 메서드

- 메서드의 선언부만 작성하고 실제 수행내용은 구현하지 않은 추상 메서드를 선언하는데 사용한다.

```java
abstract class AbstractTest {	// 추상 클래스(추상 메서드를 포함한 메서드)
	abstract void move();	// 추상 메서드(구현부가 없는 메서드)
}

// 추상 클래스는 아직 완성되지 않은 메서드가 존재하는 '미완성 설계도'이므로 인스턴스를 생성할 수 없다.
AbstractTest a = new AbstractTest();	// 에러.
```


##### 접근 제어자 (access modifier)
- 접근 제어자는 멤버 또는 클래스에 사용되어, 해당하는 멤버 또는 클래스를 외부에서 접근하지 못하도록 제한하는 역할을 한다.

- 클래스, 멤버변수, 메서드, 생성자에 접근 제어자가 지정되지 않았다면, 접근 제어자는 default라는 뜻한다.

대상 : 클래스, 멤버변수, 메서드, 생성자
private : 같은 클래스 내에서만 접근 가능
default : 같은 패키지 내에서만 접근 가능
protected : 같은 패키지 내에서, 그리고 다른 패키지의 자손클래스에서 접근 가능
public : 접근 제한이 없다.

public \> protected \> (default) \> private












