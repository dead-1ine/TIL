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

