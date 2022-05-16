

## Partition

Partition이란 DB Server에서는 데이터를 별도의 테이블로 분리해서 저장하지만 사용자는 여전히 하나의 테이블로 읽기와 쓰기를 할 수 있게 해주는 기술이다.

Partition은 DBMS 하나의 서버에서 테이블을 분산하는 것이다.



## 사용 이유

-   파티션은 데이터와 인덱스를 조각화하여 물리적 메모리를 효율적으로 사용할 수 있게 만들어준다.
-   파티셔닝하지 않고 하나의 큰 테이블로 사용하면 인덱스도 커지고 그 만큼 물리적인 메모리의 공간도 많이 필요해진다.

-   단일 INSERT, 단일 SELECT, 범위 SELECT의 빠른 처리

인덱스는 일반적으로 SELECT를 위한 것으로 보이지만 UPDATE와 DELETE, 그리고 INSERT 쿼리를 위해 필요할 때도 많다.


## 예제
```sql
SELECT 순위함수() OVER(PARTITION BY 컬럼명 ORDER BY 컬럼명)
FROM 테이블명

SELECT 집계함수(컬럼명) OVER (PARTITION BY 컬럼명)
FROM 테이블명
```

- 순위 함수
	- ROW_NUMBER
	- RANK
	- DENSE_RANK
- 집계 함수
	- SUM
	- AVG
	- MAX
	- MIN
	- COUNT

### 예제 1. 학생들의 등수 매기기
---
![[스크린샷 2022-03-27 오후 9.34.59.png]]
```sql
SELECT *, ROW_NUMBER() OVER(ORDER BY Score DESC) 'Row'
FROM TABLE_A
```
![[스크린샷 2022-03-27 오후 9.35.11.png]]
- 순위 함수인 ROW_NUMBER를 이용하면 쉽게 등수를 매길 수 있다.


### 예제 2. 학생들의 반별 등수 매기기
---
```sql
SELECT *, ROW_NUMBER() OVER(PARITION BY Class ORDER BY Score DESC) 'P_Row' FROM TABLE_A
```
![[스크린샷 2022-03-27 오후 9.36.27.png]]

### 예제 3. 반별 총 점수
---
> 해당 학생이 해당하는 반의 총 점수를 계산해보자
```sql
SELECT *, SUM(Score) OVER(PARTITION BY Class) AS 'C_Sum'
FROM TABLE_A
```
![[스크린샷 2022-03-27 오후 9.37.31.png]]