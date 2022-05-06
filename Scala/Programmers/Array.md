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
		
	}
}
```