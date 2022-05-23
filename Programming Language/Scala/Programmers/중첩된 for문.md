- for문에 여러 개의 range를 세미콜론으로 구분하여 적으면 for문을 중첩해서 사용한 것과 같은 효과를 낸다.

```scala
object LearnScala {
	def main(args: Array[String]): Unit = {
		for(a <- 1 to 3) {
			for(b <- 10 to 12) {
				println(a, b)
			}
		}
		println("중첩 for문 대신 아래와 같이 사용할 수 있다.")
		for(a <- 1 to 3; b <- 10 to 12) {
			println(a, b)
		}
	}	
}
```