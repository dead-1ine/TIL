- 내부 클래스는 클래스 내에 선언된 클래스이다.

- 장점
	1. 내부 클래스에서 외부 클래스의 멤버들을 쉽게 접근할 수 있다.
	2. 코드의 복잡성을 줄일 수 있다. (캡슐화)

```java
class A {
	...
	class B {
		...
	}
}

// 이 때 내부 클래스인 B는 외부 클래스인 A를 제외하고는 다른 클래스에서 잘 사용되지 않는 것이어야 함
```
 
##### 익명 클래스(anonymous class)
클래스의 선언과 객체의 생성을 동시에 하기 때문에 단 한번만 사용될 수 있고 오직 하나의 객체만을 생성할 수 있는 일회용 클래스

```java
new 조상클래스이름() {
	// 멤버 선언
}

new 구현인터페이스이름() {
	// 멤버 선언
}
```

```java
class AnonymousClass {
	Object tv = new Object() { void method(){} };	// 익명 클래스
	static Object cv = new Object() { void method(){} };	// 익명 클래스

	void myMethod() {
		Object lv = new Object() { void method(){} ];	// 익명 클래스
	}
}
```

```java
// 이 클래스를
class Example {
	public static void main(String[] args) {
		Button b = new Button("Start");
		b.addActionListener(new EventHandler());
	}
}

class EventHandler implements ActionListener {
	public void actionPerformed(ActionEvent e) {
		System.out.println("ActionEvent occurred!!!");
	}
}

// 이렇게 변경
class Example {
	public static void main(String[] args) {
		Button b = new Button("Start");
		b.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				System.out.println("ActionEvent occurred!!!");
			}
		}
		);
	}
}
```
