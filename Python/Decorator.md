### Decorator

---

-   구조를 수정하지 않고 기존 객체에 새로운 기능을 추가할 수 있도록 하는 Python의 디자인 패턴
-   Decorator는 일반적으로 Decorate하려는 함수의 정의 전에 호출된다.



### Example Code

---

```python
def decorator(func):
  def wrapper(*args, **kwargs):
    if checkLogin():
      func(*args, **kwargs)
    log()
  return wrapper

@decorator
def insertUser(arg):
  # do something
```



### 사용 이유

---

-   시스템이 커질수록 관리가 편하고, 런타임에 validation하기 좋다.
-   소스코드 또한 주요 로직만 보여지므로 가독성이 좋아진다.



### 두 개의 Decorator 사용

---

```python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer("Hello")

# result
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
```

