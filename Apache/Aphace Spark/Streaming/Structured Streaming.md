# Structured Streaming

Spark Streaming에는 DStreams라는 기능이 있고, 그 위에 DataFrame을 사용하여 더 간단하게 처리할 수 있는 Structured Streaming이 있다.

Stream Processing의 구성요소

- 데이터 소스
- 스트림 처리 파이프라인
- 데이터 싱크

### Read Data From Kafka with Spark

spark.readStream을 사용하여 카프카의 어떤 토픽에서 데이터를 가져올지 결정한다.

```python
kafka_server = 'kafka_server'
topic = 'topic'

df = (spark.readStream
		.format('kafka')
		.option('kafka.boostrap.servers', kafak_server)
		.option('subscribe', topic)
		.option('startingOffsets', 'earliest')
		.load()) # DataStreamReader 객체를 평가하고 데이터프레임을 반환

df.isStreaming # True
```

### Read Options

| 옵션명                  | 설명                                                       |
| ----------------------- | ---------------------------------------------------------- |
| kafka.bootstrap.servers | 카프카 서버                                                |
| subscribe               | 카프카 토픽(구독할 주체)                                   |
| startingOffsets         | Streaming App이 새로 시작될 때 적용되는 오프셋 재설정 정ㅊ |

### Kafka의 고정된 반환 컬럼

실제 보고자 하는 데이터는 value 컬럼에 존재, value를 제외한 나머지는 메타데이터로 보아도 무방

- key
- value
- topic
- partition
- offset
- timestamp
- timestampType

### writeStream

카프카 데이터는 스키마를 확인할 순 있으나 데이터 자체를 `df.show()` 로 출력할 수 없다. 그 대신 console에 출력하는 형태로 값을 확인할 수 있다.

```python
console_sink = (df.writeStream
		.queryName('kafka_console')
		.format('console')
		.option('truncate', 'false')
		.start())

console_sink.stop() # Stop streaming process
```

서버의 메모리에 write하여 쿼리하여 값을 확인할 수도 있다.

```python
memory_sink = (df.writeStrea
		.queryName('kafka_memory')
		.format('memory')
		.start())

spark.sql('SELECT * FROM kafka_memory').show()

memory_sink.stop() # Stop streaming process
```