# PyArrow의 read_table()로 Spark의 partitionby()로 적재한 parquet 파일을 읽을 때 발생한 에러

- [ ]  PyArrow의 read_table(partitioning=’hive’) 시 정수형의 기본 타입이 int32인지 알아봐야 함
- [ ]  Spark의 Type으로 적재한 Parquet 파일의 스키마 중 short를 PyArrow가 int16으로 변환하는 것인지

상황 순서:

1. PySpark로 Parquet 파일을 적재
    - Parquet 컬럼 중 year, month, day를 short로 casting함
    - 이 파일은 `prefix/year=2023/date=2023-01-01/` 의 형태로 적재되어 있음
2. PyArrow의 read_table()로 `prefix/` 를 통해 적재된 파일을 읽음 → `ArrowInvalid: Unable to merge: Field year has incompatible types:` 
    1. read_table()은 기본적으로 파일을 읽을 때 partition folder를 field로 table에 넣음
    2. 이 때 type에 대한 추론을 int32로, Parquet 파일의 short는 int16으로 변환되었음
    3. Parquet와 PyArrow의 table에 같은 field명을 가지는 year를 merge가 진행됨
    4. 이 때 에러가 발생함
