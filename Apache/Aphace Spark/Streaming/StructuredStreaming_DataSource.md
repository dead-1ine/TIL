

# Data Source

<aside> 📌 Streaming Data Producer의 데이터를 사용할 수 있는 추상화

</aside>

`sparkSession`을 사용하여 `format` 메서드로 consuming할 Streaming Source를 지정하고 해당 구성을 제공하는 빌더 메서드인 `readStream`을 사용한다.

아래 예제는 File Streaming Source를 만든다. format 메서드를 사용하여 소스 유형을 json으로 지정하고 schema 메서드로 파일 소스와 같은 특정한 유형의 소스에 필수인 데이터 스트림에 대한 스키마를 제공한다.

```python
file_stream = (spark.readStream
	.format('json') # 1
	.schema(schema) # 2
	.option('mode', 'DROPMALFORMED') # 3
	.load('/tmp/datasrc') # 4
)

file_stream # spark.sql.DataFrame(...)
```

1. `format()`: readStream할 Source의 유형을 지정한다.
2. `schema()`: 파일 소스와 같은 특정한 유형의 소스에 필수적으로 사용되는 것으로, 스트림에 대한 스키마를 제공하여 해당 스키마 이외의 데이터를 제거하는 등의 역할을 수행한다.
3. `option(’mode’, ‘DROPMALFORMED’)`: JSON format에서 사용되는 옵션으로, Source가 되는 JSON 파일에서 JSON 형식을 준수하지 않거나 제공된 스키마와 일치하지 않는 라인을 삭제하는 역할을 수행한다.
4. `load()`: builder에 제공된 option의 유효성을 확인하고 모든 항목이 확인되면 `Streaming DataFrame`을 반환한다.

`spark.readStream` 은 `DataStreamBuilder` 인스턴스를 생성한다. 이 인스턴스는 빌더 메서드 호출을 통해 제공되는 다양한 옵션을 관리하는 역할을 한다. 이 `DataStreamBuilder` 인스턴스에 대한 호출인 `load()` 는 빌더에 제공된 옵션의 유효성을 확인하고 모든 항목이 확인되면 `Streaming DataFrame`을 반환한다.

<aside> 📌 Spark DataFrame API의 read, write와 readStream, writeStream은 대응된다.

- read/write: 배치 작업
- readStream/writeStream: 스트리밍 작업

</aside>

`readStream`을 통해 생성된 `DataStreamBuilder`에 `load()`를 호출하면 `Streaming DataFrame`이 반환된다. `Streaming DataFrame`은 스트림을 단지 사용하기 위해 구체화만 한 것이므로 실제 사용되거나 처리되는 데이터가 없다. 실제 처리가 이루어지기 위해서는 `query`가 필요하다.

### readStream.format()으로 지정 가능한 Sources

------

아래의 소스들은 Spark 2.4.0 기준으로 작성한 것이다.

- File Based Streaming Source
    - JSON, ORC, Parquet, CSV, Text, TextFile
    - 파일 시스템에서 경로를 모니터링하고 그 안에 배치된 파일을 사용한다.
    - 스트리밍된 파일은 지정한 formatter에 의해 파싱된다.
- Socket
    - 소켓 연결을 통해 텍스트 데이터를 제공한다.
    - 스트리밍하기 위해 TCP 서버에 대한 클라이언트 연결을 설정한다.
- Kafka
    - Kafka에서 데이터를 consuming할 수 있도록 consumer를 생성한다.
- Rate
    - 테스트를 위한 소스로 사용한다.