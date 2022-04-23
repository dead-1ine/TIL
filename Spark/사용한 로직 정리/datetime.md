> S3에서 분할되어 있는 parquet 파일들을 spark.dataframe으로 불러올 때 편하게 날짜를 지정하여 사용하는 방법

```python
from datetime import datetime, timedelta

# 파라미터를 쉽게 넣기 위해 변수를 선언
target_date = "2022-03-30"

# 날짜 계산을 편하게 하기 위해 datetime으로 wrapping함
target_date = datetime.strptime(target_date, "%Y-%m-%d")

# S3의 파일은 시간단위로 폴더링 되어있고, 이를 앞 뒤로 한 시간 넉넉하게 가져오기 위한 file_path 설정
one_day = 26

# 0부터 one_day까지 순차적으로 1시간씩 target_date의 날짜에서 뺼셈을 진행
dates = [target_date - timedelta(hours=i) for i in range(0, one_day)]

# S3의 파일 경로 지정
path = "s3://bucket_name/file_path/{0}/{1}/{2}/{3}/*.parquet"

# S3의 지정 경로의 파라미터로 각 시간을 대입하여 경로 리스트를 생성
# ["s3://bucket_name/file_path/2022/03/31/00/*.parquet", "s3://bucket_name/file_path/2022/03/30/23/*.parquet", ...]
paths = list(map(lambda x: path.format(x.year, str(x.month).zfill(2), str(x.day).zfill(2), str(x.hour).zfill(2)), dates))

# 경로 리스트의 parquet 파일을 모두 읽어 하나의 DataFrame으로 만듦
raw_df = spark.read.parquet(*paths)
```



- 현재 사용하는 프로그램인 Amplitude는 UTC를 기준으로 데이터가 생성된다.
- 이 UTC에 9시간을 더하면 KST가 된다.



### Spark timestamp to date

---

```python
# timestamp로 되어 있는 값을 date로 변경
# timestamp가 ns로 되어 있으면 / 1000을 하면 됨
raw_df = raw_df.withColumn('receive_time', from_unixtime(col('receive_time')/1000))

# UTC에서 expr()을 활용해 9시간을 더하여 KST로 변환
raw_df = raw_df.withColumn('receive_time', col('receive_time') + expr('INTERVAL 9 HOURS'))

raw_df.select(min(col('receive_time'), max(col('receive_time')))).show()
```



