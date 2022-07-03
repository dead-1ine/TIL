- 스파크 핵심 데이터소스
    - CSV
    - JSON
    - Parquet
    - ORC
    - JDBC/ODBC 연결
    - txt
- 커뮤니티에서 만든 데이터소스
    - 카산드라
    - HBase
    - MongoDB
    - AWS Redshift
    - XML
    - 기타 등등



# 9.1 데이터소스 API의 구조



## 9.1.1 읽기 API 구조

```Python
DataFrameReader.format(...).option("key", "value").schema(...).load()
```

모든 데이터소스를 읽을 때 위와 같은 방법을 사용하며, format 메서드의 기본값은 parquet이다.



## 9.1.2 데이터 읽기의 기초

스파크는 데이터를 읽을 때 기본적으로 DataFrameReader를 사용한다. DataFrameReader는 SparkSession의 read 속성으로 접근한다. - `spark.read`

- 전반적인 코드 구성

    ```python
    spark.read.format('csv')
    	.option('mode', 'FAILFAST')
        .option('inferSchema', 'true')
        .option('path', 'path/to/file(s)')
        .schema(someSchema)
        .load()
    ```

#### 읽기 모드

외부 데이터소스에서 데이터를 읽을 때 형식에 맞지 않는 데이터를 만날 수 있다. 특히 반정형 데이터소스를 다룰 때 많이 발생한다. 읽기 모드는 스파크가 형식에 맞지 않는 데이터를 만났을 때의 동작 방식을 지정하는 옵션이다.

| 읽기 모드           | 설명                                                         |
| :------------------ | ------------------------------------------------------------ |
| permissive(default) | 오류 레코드의 모든 필드를 null로 설정하고 모든 오류 레코드를 _corrupt_record라는 문자열 컬럼에 기록한다. |
| dropMalformed       | 형식에 맞지 않는 레코드가 포함된 로우를 제거한다.            |
| failFast            | 형식에 맞지 않는 레코드를 만나면 즉시 종료한다.              |



## 9.1.3 쓰기 API 구조

데이터 쓰기의 핵심 구조는 다음과 같다.

```python
DataFrameWriter.foramt(...).option(...).partitionBy(...).bucketBy(...).sortBy(...).save()
```

모든 데이터소스에 데이터를 쓸 때 위와 같은 형식을 사용한다. format의 기본값은 parquet이다.



## 9.1.4 데이터 쓰기의 기초

데이터 쓰기는 읽기와 매우 유사하며, DataFrameReader 대신 DataFrameWriter를 사용한다. - `dataFrame.write`

- 전반적인 코드 구성

    ```python
    dataframe.writer.format('csv')
    	.option('mode', 'OVERWRITE')
        .option('dateFormat', 'yyyy-MM-dd')
        .option('path', 'path/to/file(s)')
        .save()
    ```

    

### 저장 모드

저장 모드는 스파크가 지정된 위치에서 동일한 파일을 발견했을 때의 동작 방식을 지정하는 옵션이다.

| 저장 모드              | 설명                                                         |
| ---------------------- | ------------------------------------------------------------ |
| append                 | 해당 경로에 이미 존재하는 파일 목록에 결과 파일을 추가한다.  |
| overwrite              | 이미 존재하는 모든 데이터를 완전히 덮어쓴다.                 |
| errorIfExists(default) | 해당 경로에 데이터나 파일이 존재하는 경우 오류를 발생시키면서 쓰기 작업이 실패한다. |
| ignore                 | 해당 경로에 데이터나 파일이 존재하는 경우 아무런 처리도 하지 않는다. |

기본값은 **errorIfExists**이며, 스파크가 파일을 저장할 경로에 데이터나 파일이 이미 존재하면 쓰기 작업은 그 즉시 실패한다.