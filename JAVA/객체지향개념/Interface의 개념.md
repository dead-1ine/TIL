
추상메서드의 집합
설계도

```java
interface I {
	void method();
	// public abstract가 자동으로 붙는다.

// 분리하여 보다 유연하게 사용할 수 있다.
class B implements I {
	void method() {
		System.out.println("methodInB");
	}
}
```

- 인터페이스의 장점
	1. 두 대상(객체)간의 ‘연결, 대화, 소통’을 돕는 ‘중간역할’을 한다.
	2. 선언과 구현을 분리시킬 수 있게 한다.
	3. 느슨한 결합
		```java
		class A {
			public void methodA(I i) {
				i.methodB();	// 알맹이는 바뀌었으나, A의 코드는 변경하지 않아도 된다.
			}
		}

		interface I { void methodB(); }

		// 만약 C 클래스의 구현메서드를 사용하고 싶으면 알맹이만 변경하면 클래스 A에서 변경할 코드가 없다.
		class B implements I {
			public void methodB() {
				System.out.println("methodB()");
			}
		}

		class C implements I {
			public void methodB() {
				SyStem.out.println("methodB() in C");
			}
		}
		```
	4. 개발 시간을 단축할 수 있다.
		구현 코드가 없어도 설계도를 먼저 만들 수 있으므로.
	5. 변경에 유리한 유연성있는 설계가 가능하다.
	6. 표준화가 가능하다.(JDBC)
	7. 서로 관계없는 클래스들의 관계를 맺어줄 수 있다.
		```java
		interface Repairable {}

		// Repairable이라는 공통점을 부여함
		class SCV extends GroundUnit implements Repairable {}
		class Tank extends GroundUnit implements Repairable {}
		class Dropship extends AirUnit implements Repairable {}

		// Repairable을 구현한 객체만 가능
		void repair(Repairalbe r) {
			if (r instanceof Unit) {
				Unit u = (Unit)r;
				while(u.hitPoint != u.MAX_HP) {
					u.hitPoint++;	// Unit의 HP를 증가
				}
			}
		}	// repair(Repairable r)
		```

### 다형성(Polymorphism) - 매우 중요
- 여러 형태를 가질 수 있다.
- 조상 타입 참조 변수로 자손 타입 객체를 다루는 것