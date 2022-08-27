# SQL 문법 순서

SQL의 구문에는 실행되는 순서가 있다.



- 일반적인 쿼리 작성 문법은 다음과 같다.

```sql
SELECT column
FROM table
WHERE statement
GROUP BY column
HAVING grouping statement
ORDER BY column
```



위 쿼리의 실행 순서는 다음과 같은 순서로 이루어진다.

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT 
6. ORDER BY



## 각 쿼리 실행 순서 내용

1. **FROM** : SQL은 테이블을 가장 먼저 확인한다.(어떤 테이블에서 **SELECT**와 같은 쿼리를 실행해야하는지 제일 먼저 알아야 하기 때문)
2. **WHERE** : **FROM**으로 정한 테이블에 어떤 조건을 줄 지 정한다.
3. **GROUP BY** : **WHERE**로 조건을 준 후 공통적인 데이터끼리 묶어 그룹을 만든다.
4. **HAVING** : 공통적인 데이터가 묶인 그룹 중 주어진 조건에 맞는 그룹을 추출한다.
5. **SELECT** : 최종적으로 위 쿼리 키워드로 추출된 데이터를 선택하여 조회한다.
6. **ORDER BY** : **SELECT**로 선택한 데이터를 특정 조건으로 정렬한다.



**SELECT** 다음으로 오는 구문은 **ORDER BY** 뿐이다. 
위 쿼리 순서에 따라, **SELECT**에서 사용되는 **AS** 키워드로 alias된 컬럼명은 오직 **ORDER BY** 키워드로만 사용할 수 있다.