## 개요

---

체인 디버깅을 위한 또 다른 옵션은 .pipe 메서드를 호출해 중간값을 표시하는 것이다.

Series에 대한 .pipe 메서드에는 Series를 입력으로 취하는 함수를 전달해야만하고 함수의 출력은 무엇이든 가능하다.

(하지만 메서드 체인에서 사용하려는 경우 Series를 반환하고자 할 것이다.)



-   함수 debug_ser는 중간 과정의 값을 출력한다.

```python
>>> def debug_ser(series):
    	print("Before")
	    print(series)
	    print("After")
    	return series

>>> fb_likes.fillna(0).pipe(debug_ser).astype(int).head()
Before
# fillna()로 변경된 값
After
# astype()으로 변경된 값.head()
```



-   중간값을 저장하는 전역 변수를 생성하려면 그 또한 .pipe를 사용할 수 있다.

```python
>>> intermediate = None
>>> def get_intermediate(serires):
    	global intermediate
        intermediate = series
        return series
    
>>> res = (
		fb_likes.fillna()
		.pipe(get_intermediate)
		.astype(int)
		.head()
	)

>>> intermeidate
# 정보 출력
```

