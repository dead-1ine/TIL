- Array, List, Set, Map의 구성요소는 어떤 타입이든 사용할 수 있다.
- 하지만, 최종 타입은 공통으로 상속받는 타입 중 최상위 타입으로 결정된다.



```scala
object LearnScala {
    class Animal()
    class Dog() extends Animal()
    
    def main(args: Array[String]): Unit = {
        // Animal과 Dog가 공통으로 상속받는 최상위 타입은 Animal이므로, 아래 코드는 정상실행된다.
        val array: Array[String] = Array(new Animal(), new Dog())
        // val wrongArray: Array[Dog] = Array(new Animal(), new Dog()) // 올바르지 않은 타입이다.
        
        // List도 같은 원리로 동작
        val list: List[Animal] = List(new Animal(), new Dog())
        
        // Map도 같은 원리로 동작
        val map:[String, Animal] = Map("Animal" -> new Animal(), "Dog" -> new Dog())
        
    }
}
```

