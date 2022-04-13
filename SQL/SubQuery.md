## 서브쿼리란?

---

하나의 SQL 문에 포함되어 있는 또 다른 SQL문을 말한다.



## 서브쿼리의 분류

---

### 단일 행 서브쿼리

```sql
SELECT c1, c2, c3
FROM t1
WHERE c1 = (SELECT c1
           FROM t2
           WHERE c2 = '3')
ORDER BY c1, c2, c3
```



-   그룹 함수를 사용하는 경우 결과값이 1건이기 때문에 단일 행 서브쿼리로써 사용이 가능하다.

```sql
SELECT c1, c2, c3
FROM t1
WHERE c1 <= (SELECT AVG(c1)
            FROM t2
            WHERE c2 = '3')
ORDER BY c1, c2, c3;
```



### 다중 행 서브쿼리

서브쿼리의 결과가 2건 이상 반환될 수 있다면 반드시 다중 행 비교 연산자(IN, ALL, ANY, SOME)와 함께 사용해야 한다.

| 다중 행 연산자 | 설명                                                         |
| -------------- | ------------------------------------------------------------ |
| IN             | 서브쿼리의 결과에 존재하는 임의의 값과 동일한 조건을 의미한다. |
| ALL            | 서브쿼리의 결과에 존재하는 모든 값을 만족하는 조건을 의미한다. |
| ANY            | 서브쿼리의 결과에 존재하는 어느 하나의 값이라도 만족하는 조건을 의미한다. |
| EXISTS         | 서브쿼리의 결과를 만족하는 값이 존재하는지 여부를 확인하는 조건을 의미한다. |

-   만약 T2 테이블의 C2 = 3인 조건을 만족하는 C1의 값이 2건 이상인 경우 = 이 아닌 IN을 사용해야 한다.

```sql
SELECT C1, C2, C3
FROM T1
WHERE C1 IN (SELECT C1
            FROM T2
            WHERE C2 = '3')
ORDER BY C1, C2, C3;
```



### 다중 컬럼 서브쿼리

-   서브쿼리 결과로 여러 개의 컬럼이 반환되어 메인쿼리의 조건과 동시에 비교되는 것을 의미한다.

```sql
SELECT C1, C2, C3
FROM T1
WHERE (C1, C2) IN (SELECT C1, C2
                  FROM T2
                  WHERE C2 = '3')
ORDER BY C1, C2, C3;
```



### 연관 서브쿼리

-   서브쿼리 내에 메인쿼리 컬럼이 사용된 서브쿼리이다.

```sql
SELECT T1.C1, T1.C2, T1.C3
FROM T1 T1
WHERE (T1.C1, T1.C2) IN (SELECT T2.C1, T2.C2
                        FROM T2 T2
                        WHERE T2.C2 = T1.C2) -- 메인 쿼리의 컬럼을 서브쿼리에 사용
ORDER BY T1.C1, T1.C2, T1.C3;
```



## 그 밖의 위치에서 사용하는 서브쿼리

---

### SELECT 절에 사용하는 서브쿼리

-   스칼라 서브쿼리는 한 행, 한 컬럼만을 반환하는 서브쿼리이다.

```sql
SELECT T1.C1, (SELECT AVG(T2.C1) FROM T2 T2)
FROM T1 T1;
```



### FROM 절에 사용하는 서브쿼리

-   인라인 뷰라고 한다.
-   기본적으로 FROM 절에 테이블명이 오도록 되어있다.
-   서브쿼리가 FROM 절에 사용되면 동적으로 생성된 테이블인 것처럼 사용할 수 있다.
-   인라인 뷰는 SQL 문이 실행될 때만 임시로 생성되는 동적 뷰이기 때문에 데이터베이스에 해당 정보가 저장되지 않는다.
-   인라인 뷰는 동적으로 조인 방식을 사용하는 것과 같다.

```sql
SELECT T1.C1, T2.C1, T2.C2
FROM T1 T1,
	(SELECT C1, C2 FROM T2) T2
WHERE T1.C1 = T2.C1;
```

