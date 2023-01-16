파이썬의 클래스를 쓰다보면 상속을 받게 되는 일이 많다. 어떤 상속에서는 super()를 쓰고, 어떤 상속에서는 super(class, self)를 사용한다. 

```python
class Human:
    """ Super Class """
    def __init__(self):
        self.name = '사람 이름'
        self.age = '나이'
        self.city = '도시'
        
    def show(self):
        print("사람 클래스의 메서드입니다.")
        
class Student(Human):
    """ Child Class """
    def __init__(self, name):
        super().__init__()
        self.name = name
        
   	def show_name(self):
        print("사람의 이름은:", self.name)
    
    def show_age(self):
        print("사람의 나이는:", self.age)
        
        
a = Student('james')
a.show() # 메소드 상속
a.show_age() # 인스턴스 속성 상속
a.show_name() # 자식노드에서 속성을 변경
```

```console
사람 클래스의 메서드입니다.
사람의 나이는: 나이
사람의 이름은: james
```



```python
class Human:
    """ Super Class """
    def __init__(self):
        self.name = '사람이름'
        self.age = '나이'
        self.city = '사는 도시'
    
    def show(self):
        print("사람 클래스의 메서드입니다.")
        
class Student(Human):
    """ Child Class """
    def __init__(self, name):
        super(Student, self).__init__()
        self.name = name
    
    def show_name(self):
        print("사람의 이름은:", self.name)
        
    def show_age(self):
        print("사람의 나이는:", self.age)


a = Student('james')
a.show() # 메서드 상속
a.show_age() # 인스턴스 속성 상속
a.show_name() # 자식노드에서 속성을 변경
```

```console
사람 클래스의 메서드입니다.
사람의 나이는: 나이
사람의 이름은: james
```



`super(Student, self).__init__()`: 자식 클래스가 상속받는 부모 클래스를 자식 클래스에 불러오겠다는 의미이다.