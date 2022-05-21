- 변경할 수 없는(immutable) Collection이 `var`로 선언된 경우 Collection에 `+=` 연산자나 `-+` 연산자를 사용할 수 있다.
- 하지만 Collection 자체가 변경할 수 없는 형태이므로 이 때는 변경사항을 반영한 새로운 Collection이 만들어져 var로 선언된 변수에 저장된다.



- 변경할 수 있는(mutable) Collection의 경우 `+=` 나 `-=` 연산자가 Collection의 메서드로 동작한다.



```scala
import scala.collection.mutable

object LearnScala {
    def main(args: Array[String]): Unit = {
        // 1. 변경할 수 없는 Collection이 var로 선언된 경우
        var immutableSet = Set(1, 2, 3)
        immutableSet += 4
        
        
    }
}
```

