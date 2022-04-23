- pyspark.sql.functions.split

  spark의 데이터프레임에서 string형으로 되어있는 컬럼의 값을 list로 반환한다.

- pyspark.sql.functions.size
  spark의 데이터프레임 중 list형으로 되어있는 값의 총 길이를 반환한다.
- pyspark.sql.functions.trim
  컬럼의 값에서 공백을 제거한다.

```python
raw_df = (raw_df
          	.select(
              col('receive_time'),
              split(col('event_type'), '-')).alias('event_type_array'),
          		size(split(col('event_type'), '-')).alias('event_type_len'))
						.withColumn('event_type_1', trim(col('event_type_array')[0]))
  					.withColumn('event_type_2', when(col('event_type_len') == 2, trim(col('event_type_array')[1])).otherwise('NONE'))
    				.withColumn('event_type_3', when(col('event_type_len') == 2, trim(col('event_type_array')[2])).otherwise('NONE'))
```