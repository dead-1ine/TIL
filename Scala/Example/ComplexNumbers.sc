// 인자 없는 함수
object ComplexNumbers {
    def main(args: Array[String]): Unit = {
        val c = new Complex(1.2, 3.4)
        println("Imaginary Part: " + c.im())
    }
}