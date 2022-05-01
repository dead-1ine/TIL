- 조건문은 Java나 C와 유사하다.

- 스칼라에서 중요한 차이점은 if문도 수식이라는 점이다.
- 코드의 16번째 줄과 같이 if문만으로 삼항 연산자를 대신할 수 있다.

```scala
object LearnScala {
	def main(args: Array[String]): Unit = {
		if(true)
			println("한 줄은 {}를 생략할 수 있다.")
			
		if(1 + 1 = 2) {
			println("여러 줄은")
			println("{}가 필요하다.")
		} else {
			println("컴퓨터가 미쳤나봐요.")
		}
		
		val likeEggs = false
		// 삼항 연산자 대신 이렇게 사용할 수 있다.
		val breakfast =
			if(likeEggs) "계란후라이"
			else "사과"
		
		println(s"아침으로 ${breakfast}를 먹어요.")
	}
}
```