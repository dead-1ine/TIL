
- 인터페이스는 추상메서드의 집합, 설계도라고 한다.

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
	- 개발시간을 단축시킬 수 있다.
	- 표준화가 가능하다.
	- 서로 관계없는 클래스들에게 관계를 맺어 줄 수 있다.
	- 독립적인 프로그래밍이 가능하다.

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

##### 인터페이스의 상속
- 인터페이스는 인터페이스로만 상속받을 수 있다.
- 클래스와 달리 다중상속이 가능

```java
interface Movable {
	/* 지정된 위치(x, y)로 이동하는 기능의 메서드 */
	void move(int x, int y);
}

interface Attackable {
	/* 지정된 대상(u)을 공격하는 기능의 메서드 */
	void attack(Unit u);
}

interface Fightable extends Movable, Attackable { }
```

- 클래스의 상속과 마찬가지로 자손 인터페이스는 조상 인터페이스에 정의된 멤버를 모두 상속받는다.

##### 인터페이스를 이용한 다형성

```java
// 인터페이스 Fightable을 클래스 Fighter가 구현했을 때, Fighter인스턴스를 Fightable타입의 참조변수로 참조하는 것이 가능하다.
Fightable f = (Fightable) new Fighter();
Fightable f = new Fighter();

// 인터페이스는 다음과 같이 메서드의 매개변수의 타입으로도 사용될 수 있다.
void attack(Fightable f) {
	// ...
}

// 인터페이스 타입의 매개변수가 갖는 의미는 메서드 호출 시 해당 인터페이스를 구현한 클래스의 인스턴스를 매개변수로 제공해야 한다는 것이다.
class Fighter extends Unit implements Fightable {
	public void move(int x, int y) { /* 생략 */ }
	public void attack(Fightable f) { /* 생략 */ }
}

// 
```
