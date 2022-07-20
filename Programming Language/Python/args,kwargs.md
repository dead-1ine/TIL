# *args, **kwargs

둘 다 파라미터의 길이를 특정하기 어려울 때 사용한다.

```python
def number_and_name(*args **kwargs):
   	print(args, kwargs)
    
number_and_name(1, 2, 3, name='홍길동')

# 키워드 없이 전달하면 *args로 전달되고 키워드 파라미터로 전달하면 **kwargs로 전달된다.
# (1, 2, 3) {'name': '홍길동'}
```



