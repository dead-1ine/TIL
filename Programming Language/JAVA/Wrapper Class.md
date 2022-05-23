> 8개의 기본형을 객체로 다뤄야할 때 사용하는 클래스
> ```java
> public final class Integer extends Number implements Comparable {
> 	private int value;
> }
> ```

- 오토박싱 & 언박싱
	> 컴파일러가 자동으로 typeValue();해준다.
 - 오토박싱(autoboxing) : 기본형 값을 래퍼 클래스의 객체로 자동 변환해주는 것
- 언박싱(unboxing) : 반대로 변환하는 것
	```java
	ArrayList<Integer> list = new ArrayList<Integer>();
	list.add(10);		// 오토박싱. 10 -> new Integer(10);

	int value = list.get(0);	// 언박싱. new Integer(10) -> 10
	```
