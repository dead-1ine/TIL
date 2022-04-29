- 스칼라는 Range와 List를 생성하고 다루는 유용한 도구들을 제공한다.

- 사용한 함수
	- to
		Range를 생성한다.
	- until
		마지막 숫자를 포함하지 않는 Range를 생성한다.
	- by
		조건의 수만큼 건너뛰는 Range를 생성한다.
	- toList
		List로 변환한다.
	- filter
		조건에 맞는 것만 반환한다.
	- map
		전달받은 iterable 값의 아이템을 순회한다.

```scala
object LearnScala {
	def main(args: Array[String]): Unit = {
		// 1. to를 이용하면 1부터 10을 포함하는 Range를 생성한다.
		val range1 = 1 to 10
		println(s"1. 1 to 10 -> $range1")
		
		// 2. until을 이용하면 마지막 숫자를 포함하지 않는 Range를 생성한다.
		val range2 = 1 until 10
		println(s"2. 1 until 10 -> $range2")
		
		// 3. by를 이용하면 숫자를 건너뛰는 Range를 생성한다.
		val range3 = 1 until 10 by 3
		println(s"3. 1 until 10 by 3 -> $range3")
		
		// 4. toList를 통해 List로 변환한다.
		println(s"4. range1.toList -> ${range1.toList}")
		
		// 5. filter: 조건에 맞는 것만 모은다.
		val moreThan4 = range1.filter(_ > 4)
		println(s"5. range1.filter(_ > 4) -> $moreThan4")
		
		// 6. map: 각 아이템의 값을 변경한다.
		val doubleIt = range1.map(_ * 2)
		println(s"6. range1.map(_ * 2) -> $doubleInt")
	}
}
```