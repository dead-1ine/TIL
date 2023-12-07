- JPerson.scala

```scala
class JPerson() {
    var _name: String = null
    def this(_name: String) = {
        this()
        	this._name = _name
    }
    
    // 스칼라 스타일의 getter, setter
    def name_ = (_name: String) = this._name = _name
    def name = this._name
    
    // 자바 스타일의 getter, setter
    def getName() = name
    def setName(name: String) = this.name = name
}
```

- LearnScala.scala

```scala
object LearnScala {
    def main(args: Array[String]): Unit = {
		val jp = new JPerson("Java Style")
        val sp = new SPerson("Scala Style")
        
        println(jp.name)
        println(sp.name)
        
        jp.name += " Hate this!"
        sp.name += " Like this!"
        
        println(jp.getName)
        println(sp.getName)
    }
}
```

- SPerson.scala

```scala
// This is the simple way on scala
import beans._
class SPerson(@BeanProperty var name: String)
// @BeanProperty는 필수가 아니다. 자바 스타일의 getter와 setter가 필요한 경우에만 사용
```

