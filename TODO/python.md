

### @classmethod



### @staticmethod

------

staticmethod는 정적 메서드를 의미하며, self 파라미터를 갖지 않고 인스턴스 변수에 접근할 수 없다. 따라서, 정적 메서드는 보통 객체 필드와 독립적이지만 로직 상 클래스 내에 포함되는 메서드에 사용된다. 정적 메서드는 메서드 앞에 @staticmethod라는 Decorator를 표시하여 해당 메서드가 정적 메서드임을 표시한다.