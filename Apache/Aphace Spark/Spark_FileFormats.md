## 9.2 CSV 파일

CSV(Comma-Separated Values)는 콤마로 구분된 값을 의미한다. CSV는 각 줄이 단일 레코드가 되며 레코드의 각 필드를 콤마로 구분하는 일반적인 텍스트 파일 포맷이다. CSV 파일은 구조적으로 보이지만, 매우 까다로운 포맷 중 하나이다.

그 이유는 운영 환경에서는 어떤 내용이 들어 있는지, 어떠한 구조로 되어 있는지 등 다양한 전제를 만들 수 없기 때문이다. 그러한 이유로 CSV reader는 많은 수의 옵션을 제공한다.

예를 들어, CSV 파일 내 컬럼 내용에 콤마가 들어있거나 비표준적인 방식으로 null 값이 기록된 경우 특정 문자를 이스케이프 처리하는 옵션을 사용해 문제를 해결할 수 있다.




### 9.2.1 CSV Option

| 읽기/쓰기 | 키                          | 사용 가능한 값                                         | 기본값                       | 설명                                                         |
| --------- | --------------------------- | ------------------------------------------------------ | ---------------------------- | ------------------------------------------------------------ |
| 모두      | sep                         | 단일 문자                                              | ,                            | 각  필드와 값을 구분하는 데 사용되는 단일 문자               |
| 모두      | header                      | true, false                                            | false                        | 첫 번째 줄이 컬럼명인지 나타내는 불리언값                    |
| 모두      | nullValue                   | 모든 문자열                                            | ""                           | 파일에서 null 값을 나타내는 문자                             |
| 모두      | nanValue                    | 모든 문자열                                            | NaN                          | CSV 파일에서 NaN이나 값이 없음을 나타내는 문자를 선언        |
| 모두      | positiveInf                 | 모든 문자열 또는 문자                                  | Inf                          | 양의 무한 값을 나타내는 문자(열)를 선언                      |
| 모두      | negativeInf                 | 모든 문자열 또는 문자                                  | -Inf                         | 음의 무한 값을 나타내는 문자(열)를 선언                      |
| 모두      | compression 또는 codec      | [none, uncompre, bzip2, deflate, gzip, lz4,snappy]     | none                         | 스파크가 파일을 읽고 쓸 때 사용하는 압축 코덱을 정의         |
| 모두      | dateFormat                  | 자바의 SimpleDateFormat을 따르는 모든 문자열 또는 문자 | yyyy-MM-dd                   | 날짜 데이터 타입인 모든 필드에서 사용할 날짜 형식            |
| 모두      | timestampFormat             | 자바의 SimpleDateFormat을 따르는 모든 문자열 또는 문자 | yyyy-MM-dd'T'HH:mm:ss.SSSSZZ | 타임스탬프 데이터 타입인 모든 필드에서 사용할 날짜 형식      |
| 읽기      | escape                      | 모든 문자열                                            | \                            | 스파크가 파일에서 이스케이프 처리할 문자                     |
| 읽기      | inferSchema                 | true, false                                            | false                        | 스파크가 파일을 읽을 때 컬럼의 데이터 타입을 추론할지 정의   |
| 읽기      | ignoreLeadingWhiteSpace     | true, false                                            | false                        | 값을 읽을 때 값의 선행 공백을 무시할지 정의                  |
| 읽기      | ignoreTrailingWhiteSpace    | true, false                                            | false                        | 값을 읽을 때 값의 후행 공백을 무시할지 정의                  |
| 읽기      | maxColumns                  | 모든 정수                                              | 20480                        | 파일을 구성하는 최대 컬럼 수를 선언                          |
| 읽기      | maxCharPerColumn            | 모든 정수                                              | 10000000                     | 컬럼의 문자 최대 길이를 선언                                 |
| 읽기      | escapeQuotes                | true, false                                            | true                         | 스파크가 파일의 라인에 포함된 인용부호를 이스케이프할지 선어 |
| 읽기      | maxMalformedLogPerPartition | 모든 정수                                              | 10                           | 스파크가 각 파티션별로 비정상적인 레코드를 발견했을 때 기록할 최대수. 이 숫자를 초과하는 비정상적인 레코드는 무시됨 |
| 읽기      | multiLine                   | true, false                                            | false                        | 인용부호 문자가 있는 값을 이스케이프 처리하지 않고, 전체 값을 인용 부호로 묶을지 여부 |
| 쓰기      | quoteAll                    | true, false                                            | false                        | 하나의 논리적 레코드가 여러 줄로 이루어진 CSV 파일 읽기를 허용할지 여부 |



### 9.2.2 CSV 파일 읽기

```python
spark.read.format('csv')
```

- 예제

    ```python
    spark.read.format('csv')
    	.option('header', 'true')
        .option('mode', 'FAILFAST')
        .option('inferScheam', 'true')
        .load('some/path/to/file.csv')
    ```



다음과 같이 읽기 모드와 생성한 스키마를 파일의 데이터가 예상한 형태로 이루어져 있음을 검증하는 용도로 사용할 수 있다.

```python
from pyspark.sql.types import StructField, StructType, StringType, LongType

my_manual_schema = new StructType([
    StructField('DEST_COUNTRY_NAME', StringType(), True),
    StructField('ORIGIN_COUNTRY_NAME', StringType(), True),
    StructField('count', LongType(), False)
])

(spark.read.format('csv')
	.option('header', 'true')
	.option('mode', 'FAILFAST')
	.schema(my_manual_schema)
	.load(file_path)
	.show(5))
```

스파크는 **지연 연산** 특성이 있어 DataFrame 정의 시점이 아닌 잡 실행 시점에만 오류가 발생한다.



### 9.2.3 CSV 파일 쓰기

읽기와 마찬가지로  CSV 파일을 쓸 때 사용할 수 있는 다양한 옵션이 있다. maxColumns와 inferSchema 옵션 같이 데이터 쓰기에는 적용되지 않는 옵션을 제외하면 읽기와 동일한 옵션을 제공한다.

- 쓰기 예제

    ```python 
    csv_file = (spark.read.format('csv')
               		.option('header', 'true')
               		.option('mode', 'FAILFAST')
               		.option('inferSchema', 'true')
                	.schema(my_manual_schema)
               		.load(read_file_path)) # file.csv
    ```

- 그리고 CSV 파일을 읽어 들여 TSV 파일로 내보내는 처리도 간단하다.

```python
csv_file.write.format('csv').mode('overwrite').option('seq', '\t').save(write_file_path) # file.tsv
```

​	이 명령은 실제로 데이터를 쓰는 시점에 DF의 파티션 수를 반영한다. 만약 사전에 데이터를 분할했다면 파일 수가 달라졌을 것이다.

