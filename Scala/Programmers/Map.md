- Map은 `Map(Key1 -> Value1, Key2 -> Value2, ...)`와 같이 생성한다.

- 스칼라에서 기본 Map은 Predef.Map(scala.collection.immutable.Map)이다.

- Map도 Set과 마찬가지로 구성요소가 4개일 때까지 Map1, Map2, Map3, Map4라는 별도 클래스로 구현되지만 더 많아지면 HashMap으로 구현된다.

- 키는 중복될 수 없으며, Set과 마찬가지로 순서가 보장되지 않는다.



```scala
obejct LearnScala {
	def main(args: Array[String]): Unit = {
        // 1. Map[String, Int]
        val map1 = Map("one" -> 1, "two" -> 2, "three" -> 3)
        // Map[Any, Any]
        val map2 = Map(1 -> "one", "2" -> 2.0, "three" -> false)
        println(s"1. $map1")
        
        // 2. 중복된 키가 있으면 마지막 값을 사용
        println(s"2. ${Map('a' -> 1, 'a' -> 2)}")
        
        // 3. key를 가지고 값 읽어오기
        val one = map1("one")
        println(s"3. ${one}")
        
        /* 4. 키가 없으면 NoSuchElementException이 발생함
         * 예를 들어 val fourExists = map1("four")
         * get()을 이용해 얻는 객체의 isDefine 값으로 Key가 있는지 확인 */
        val fourExistsOption = map1.get("four")
        println(s"4. ${fourExistsOption.isDefined}")
        
        // 5. ++연산자로 두 개의 Map을 더할 수 있으며, 중복된 키("three")의 값은 마지막 값으로 결정
        val concatenated = map1 ++ map2
        println(s"5. ${concatenated}")
        
        // 6. find(List, Set과 같은 형태)
        val personMap = Map(("솔라", 1), ("문별"), 2), ("휘인", 3))
        def findByName(name: String) = personMap.getOrElse(name, 4)
        val findSolar = findByName("솔라") // 값 1을 찾아 넘겨줌
        val findSun = findByName("태양") // 값이 없으므로 4를 넘겨줌
        println(s"6. ${findSolar}, ${findSun}")
    }
}
```

