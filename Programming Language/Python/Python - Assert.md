# Python - Assert

Assert는 어떤 조건이 True임을 보증하기 위해 사용하는 키워드이다.

Assert는 이 조건이 참일 때 코드는 내가 보장한다. 이 조건은 올바르다. 를 의미한다.

하지만, 이 조건이 거짓이라는 것은 내가 보증하지 않은 동작이다. 그러니 Assertion Error를 발생시켜라.



## Assert 사용법

```python
assert [조건], [오류 메시지]
```

- [조건]: 이 조건이 True이면 코드가 그대로 진행되고, False라면 Assertion Error가 발생한다.
- [오류 메시지]: 앞 조건이 False인 경우 "Assertion Error와 함께 남긴 메시지"를 발생시킨다. (생략 가능)



```python
name = "2BlockDMask"
assert name[0].isalpha(), "이름의 맨 처음은 알파벳으로 시작해주세요."
```

