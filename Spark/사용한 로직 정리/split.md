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

