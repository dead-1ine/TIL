# 제어자 (Modifier)

##### static - 클래스의, 공통적인

사용 장소 : 멤버변수, 메서드, 초기화 블럭

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
