### 형식

```sql
SELECT expr1, expr2, ...
	FROM ...
	WHERE ...
	AND ...
GROUP BY expr1, expr2, ...
ORDER BY ...
```



### 쿼리 1

```sql
SELECT station_name
	FROM subway_statistics
WHERE gubun = '승차'
GROUP BY station_name
```

| station_name  |
| :-----------: |
| 가락시장(340) |
|   강남(222)   |
|   강변(214)   |
| 건대입구(212) |



- Gruop By 절은 집계 함수와 같이 사용해야 의미가 있다.
- 집계 함수는 SQL 함수의 일종으로 테이블에 있는 데이터의 전체 건수를 구하거나 특정 컬럼의 최댓값, 최솟값, 평균 등을 구하는 함수이다.



### 집계함수

---

- COUNT(expr)

  expr의 전체 개수를 반환한다.

- MAX(expr)

  expr의 최댓값을 반환한다.

- MIN(expr)

  expr의 최솟값을 반환한다.

- SUM(expr)

  expr의 합계를 반환한다.

- AVG(expr)

  expr의 평균값을 반환한다.

- VARIANCE(expr)

  expr의 분산을 반환한다.

- STDDEV(expr)

  expr의 표준편차를 반환한다.

이외에도 여러 집계 함수가 있지만 위 6개가 제일 많이 사용된다.



#### 집계 함수

```sql
SELECT COUNT(*) cnt
	,MIN(passenger_number) min_value
	,MAX(passenger_number) max_value
	,SUM(passenger_number) sum_value
	,AVG(passenger_number) avg_value
FROM subway_statistics;
```

| CNT  | MIN_VALUE | MAX_VALUE | SUM_VALUE | AVG_VALUE |
| ---- | --------- | --------- | --------- | --------- |
| 2142 | 8         | 17062     | 2719677   | 1269.6904 |



### 조건 연산자

| 조건 연산자 | 기능                                      |
| ----------- | ----------------------------------------- |
| =           | 두 값이 같을 때 참                        |
| !=, <>      | 두 값이 다를 때 참                        |
| >           | 왼쪽 값이 오른쪽 값보다 클 때 참          |
| <           | 왼쪽 값이 오른쪽 값보다 작을 때 참        |
| >=          | 왼쪽 값이 오른쪽 값보다 크거나 같을 때 참 |
| <=          | 왼쪽 값이 오른쪽 값보다 작거나 같을 때 참 |



### 잠실역에서 7시나 9시에 승차한 건을 조회

```sql
SELECT *
	FROM subway_statistics
WHERE station_name = '잠실(216)'
AND boarding_time = 7
OR boarding_time = 9;
```

위 쿼리 결과는 잠실역에서 7시에 승하차한 건과 역에 상관없이 9시에 승하차한 건이 모두 조회된다. 이렇게 된 원인은 OR 조건 때문인데, 원래 의도대로 나오게 하려면 아래 쿼리처럼 OR 조건을 괄호에 묶어야 한다.



### 잠실역에서 7시나 9시에 승하차한 건을 조회하는 올바른 쿼리

```sql
SELECT *
	FROM subway_statistics
WHERE station_name = '잠실(216)'
	AND (boarding_time = 7
        OR boarding_time = 9);
```



## LIKE 연산자

---

-   '~와 같다'라는 의미의 연산자이다.

### 예시

```sql
WHERE station_name LIKE '선릉%'
```

-   선릉으로 시작되는 모든 건을 조회한다는 의미이다.
-   여기서 '%'는 모든 것을 의미한다.



### LIKE 연산자 사용

```sql
SELECT *
	FROM subway_statistics
WHERE station_name LIKE '잠실%';
```



## IN 연산자

---

-   예를 들어 7시와 9시 모두 조회해야 하는 조건에는 OR 연산자를 사용하면 된다.
-   하지만 OR 연산자는 어렵지는 않지만 읽기에 혼동된다는 단점이 있다.
-   바로 IN 연산자이다.

### 선릉역에서 7시와 9시 승하차 건을 조회

```sql
SELECT *
	FROM subway_statistics
WHERE station_name LIKE '선릉%'
	AND boarding_time IN (7, 9);
```

-   OR 대신 IN을 사용하면 문장이 훨씬 깔끔해진다.
-   특히 비교할 값이 많은 경우 더욱 그렇다.



## BETWEEN 연산자

---

-   이상, 이하를 조회하려면 >=와 <= 연산자를 사용하면 되지만, 좀 더 간단히 사용할 수 있는 것이 '~ 사이에'라는 뜻인 BETWEEN 연산자이다.
-   이 연산자는 '컬럼 BETWEEN a AND b' 형태로 사용한다.



### BETWEEN 연산자 사용

```sql
SELECT *
	FROM subway_statistics
WHERE station_name LIKE '선릉%'
	AND passenger_number BETWEEN 500 AND 1000;
```



