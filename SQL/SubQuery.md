## 서브쿼리란?

---

하나의 SQL 문에 포함되어 있는 또 다른 SQL문을 말한다.



## 서브쿼리의 분류

---

### 단일 행 서브 쿼리

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

