// Scala는 객체지향적 언어이며 클래스의 개념이 존재한다.
// Scala의 클래스 정의는 Java의 클래스 정의와 유사하다.
// 한가지 중요한 차이점은 Scala 클래스의 경우 파라미터를 가질 수 있다는 것인데 아래 예제로 알 수 있다.
class Complex(real: Double, imagniary: Double) {
    def re() = real
    def rm() = imaginary
}