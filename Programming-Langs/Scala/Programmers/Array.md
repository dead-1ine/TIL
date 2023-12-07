- 배열은 `Array(element1, element2, ...)`와 같이 만들 수 있다.

- 스칼라의 배열은 자바의 배열에 대응하는 개념이다.
- 예를 들어 자바에서의 `int[]`는 스칼라에서 `Array[Int]` 와 같다.

- 스칼라의 배열은 mutable이다. 사이즈를 변경할 수 있다는 의미가 아니라 들어있는 값을 변경할 수 있다는 의미의 mutable이다.\

- 배열은 그냥 출력하면 배열의 내용을 출력해주지 않는다.
- 내용을 출력하려면 `.mkString(",")`와 같은 메서드를 이용해야 한다.

```scala
object LearnScala {
	// 배열의 내용을 출력하는 메서드
	def printArray[K](array: Array[K]) = println(array.mkString("Array(", ", ", ")"))

	def main(args: Array[String]): Unit = {
		
		// 1. Array[Int]
		val array1 = Array(1, 2, 3)
		print("1 ")
		printArray(array1)
		
		// 2. Array[Any]
		val array2 = Array("a", 2, true)
		print("2 ")
		
		// 3. 배열의 값을 읽고 쓰기
		val itemAtIndex0 = array1(0)
		array1(0) = 4
		print("3 ")
		printArray(array1)
		
		// 4. 배열을 붙일 때는 ++ 연산자를 이용한다.
		// 앞에 붙일 때는 +:, 뒤에 붙일 때는 :+ 연산자이다.
		val concatenated = "앞에 붙이기" +: (array1 ++ array2) :+ "뒤에 붙이기"
		
		print("4 array1과 array2를 더하면: ")
		printArray(concatenated)
		
		// 값으로 index 찾기
		array2.indexOf("a")
		
		// 5. 다른 값만 가져오기
		val diffArray = Array(1, 2, 3, 4).dff(Array(2, 3))
		print("5. Array(1, 2, 3, 4).dff(Array(2, 3))의 결과: ")
		printArray(diffArray)
	
		val personArray = Array(("솔라", 1), ("문별", 2), ("휘인", 3))
		
		// 6. Find 메소드를 이용해서 findByName이라는 메서드를 생성
		// Find는 조건에 맞는 값을 찾으면 검색을 중단
		// getOrElse는 일치하는 값이 없을 경우 넘겨줄 기본 값
		// getOrElse가 없을 때 일치하는 값이 없으면 None
		def findByName(name: String) = personArray.find(_._1 == name).getOrElse(("화사", 4))
		
		val findSolar = findByname("솔라") // 값("솔라", 1)을 찾아서 넘겨줌
		val findSun = findbyName("태양") // 값이 없으므로 getOrElse에 잆는 값이 들어감
		println(findSolar)
		println(findSun)
	}
}
```