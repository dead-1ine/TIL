# Nested Function

---

-   중첩된 함수라는 뜻이다.
-   사용 이유 : 반복의 방지 및 가독성 향상

```python
def parent_function():
    def child_function():
        print("This is a child Function")
        
    child_function() # Call Child Function
parent_function() # Call Parent Func
```



### Why use nested function?

---

1.   가독성

     >   -   함수를 사용하는 이유 중 하나는 반복되는 코드블록을 함수 하나로 정의해서 효과적으로 코드를 관리하기 위해서다.
     >
     >   -   마찬가지로 중첩함수는 함수 안에 반복되는 코드가 있다면 중첩하여 선언하기 위해 부모 함수의 코드를 효과적으로 관리하고 가독성을 높일 수 있다.
     >
     >       ```python
     >       def print_all_elements(list_of_things):
     >           def print_each_element(things):
     >               for thing in things:
     >                   print(thing)
     >                   
     >           if len(list_of_things) > 0:
     >               print_each_element(list_of_things)
     >           else:
     >               print("There is nothing!")
     >       ```

2.   Closure

     >   -   Closure란, 사전적 의미로 '폐쇄'라는 뜻을 가진다.
     >   -   파이썬에서의 Closure는 어떤 것으로부터 격리해 사용한다는 느낌이 있다. - 필자
     >   -   즉, 중첩함수의 부모함수가 자신의 내부에 함수나 변수의 정보를 가두어 사용하는 것을 Closure라고 한다.
     >   -   그리고 부모함수는 중첩함수를 리턴해준다. 그리하면 부모함수의 변수를 외부로부터 직접적 접근에 대하여 격리하면서 중첩함수를 통해 격리된 부모함수의 변수를 사용한 연산은 가능하게 한다.
     >
     >   ```python
     >   def generate_power(base_numer):
     >       def nth_power(power):
     >           return base_number ** power
     >       return nth_power
     >   
     >   calculate_power_of_two = generate_power(2) # 부모함수에 인자값을 넣고 변수에 2를 넣음
     >   calculate_power_of_two(7) # 2의 7승 => 128
     >   
     >   calculate_power_of_seven = generate_power(7) # 부모함수에 인자값을 넣고 변수에 7을 넣음
     >   calculate_power_of_seven(3) # 7의 3승 => 343
     >   ```

# Closure Function

---

>   함수와 해당 함수가 가지고 있는 데이터를 함께 복사, 저장해서 별도 함수로 활용하는 기법
>
>   -   FirstClassFunction이다.

