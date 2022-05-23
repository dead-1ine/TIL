
- 미완성 설계도
- 인스턴스 생성 불가
- 미완성 메서드(추상 메서드)를 포함하고 있는 클래스

```java
abstract class 클래스이름 {
	...
	/* 주석을 통해 어떤 기능을 수행할 목적으로 작성하였는지 설명 */
	abstract 리턴타입 메서드이름();
}
```

- 추상클래서로부터 상속받는 자손클래스는 오버라이딩을 통해 조상인 추상클래스의 추상메서드를 모두 구현해주어야 한다. 
- 만일 조상으로부터 상속받은 추상메서드 중 하나라도 구현하지 않는다면, 자손클래스 역시 추상클래스로 지정해 주어야 한다.

```java
abstract class Player {
	abstract void play(int pos);
	abstract void stop();
}

class AudioPlayer extends Player {
	void play(int pos) { /* 내용 생략 */ }
	void stop()	{ /* 내용 생략 */ }
}

abstract class AbstractPlayer extends Player {
	void play(int pos) { /* 내용 생략 */ }
}
```


- 각 클래스의 공통부분을 뽑아 Unit클래스를 정의하고 상속받도록 함
```java
abstract class Unit {
	int x, y;
	abstract void move(int x, int y);
	void stop() { /* 현재 위치에 정지 */ }
}

class Marine extends Unit {
	void move(int x, int y) { /* 지정된 위치로 이동 */ }
	void stimPack() { /* 스팀팩을 사용한다. */ }
}

class Tank extends Unit {
	void move(int x, int y) { /* 지정된 위치로 이동 */ }
	void changeMode() { /* 모드를 변환한다. */ }
}

class Dropship extends Unit {
	void move(int x, int y) { /* 지정된 위치로 이동 */ }
	void load() { /* 선택된 대상을 태운다. */ }
	void unload() { /* 선택된 대상을 내린다. */ }
}

// Unit클래스 타입의 객체 배열을 통해 서로 다른 종류의 인스턴스를 하나의 묶음으로 다룰 수 있다.
public class MainClass {
	public static void main(String[] args) {
		Unit[] group = { new Marine(), new Tank(), new Dropship() };

		for (int i = 0; i < group.length; i++)
			group[i].move(100, 200);
	}
}
```
