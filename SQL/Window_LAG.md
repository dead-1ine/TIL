# Window LAG

LAG 함수는 특정 컬럼을 기준으로 직전 m번째 레코드 값을,
LEAD 함수는 직후 m번째 레코드 값을 출력하는 함수이다.



## PySpark

- row_number(): 행 번호를 매겨주는 함수
- LEAD(): 다음 행 값을 가져오는 함수
- LAG(): 이전 행 값을 가져오는 함수



- Sample Table

| user    | timestamp | shot_id |
| ------- | --------- | ------- |
| jaeyung | 12:34:54  | 123     |
| jaeyung | 12:45:34  | 234     |
| jaeyung | 12:50:55  | 456     |
| seung   | 12:55:23  | 334     |
| seung   | 13:01:34  | 523     |
| seung   | 13:12:43  | 646     |



## 1. row_number()

```python
spark.sql("""
SELECT 
	user,
	timestamp, 
	shot_id,
	row_number() over(partition by user order by timestamp) as row_number
FROM shot
""")
```

| user    | timestamp | shot_id | row_number |
| ------- | --------- | ------- | ---------- |
| jaeyung | 12:34:54  | 123     | 1          |
| jaeyung | 12:45:34  | 234     | 2          |
| jaeyung | 12:50:55  | 456     | 3          |
| seung   | 12:55:23  | 334     | 1          |
| seung   | 13:01:34  | 523     | 2          |
| seung   | 13:12:43  | 646     | 3          |



## 2. LEAD()

```python
spark.sql("""
SELECT
	user,
	timestamp,
	shot_id,
	lead(shot_id) over(partition by user order by timestamp) as lead_shot_id
FROM shot
""")
```

| user    | timestamp | shot_id | lead_shot_id |
| ------- | --------- | ------- | ------------ |
| jaeyung | 12:34:54  | 123     | 234          |
| jaeyung | 12:45:34  | 234     | 456          |
| jaeyung | 12:50:55  | 456     | null         |
| seung   | 12:55:23  | 334     | 523          |
| seung   | 13:01:34  | 523     | 646          |
| seung   | 13:12:43  | 646     | null         |



## 3. LAG()

```python
spark.sql("""
SELECT 
	user,
	timestamp,
	shot_id,
	lag(shot_id) over(partition by user order by timestamp) as lag_shot_id
FROM shot
""")
```

| user    | timestamp | shot_id | lag_shot_id |
| ------- | --------- | ------- | ----------- |
| jaeyung | 12:34:54  | 123     | null        |
| jaeyung | 12:45:34  | 234     | 123         |
| jaeyung | 12:50:55  | 456     | 234         |
| seung   | 12:55:23  | 334     | null        |
| seung   | 13:01:34  | 523     | 334         |
| seung   | 13:12:43  | 646     | 523         |