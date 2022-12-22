------

<aside> 💡 Spark SQL 추상화 위에 구축된 스트림 프로세서

</aside>

### Spark stream component

------

Spark Streaming에는 세 가지의 요소가 존재한다.

- Data Source

- Streaming Processing Pipeline

- Data Sink

- 단순화된 스트리밍 모델

    <aside> ⏩ Data Source → Streaming Processing Pipeline → Data Sink

    </aside>

스파크에는 두 가지의 Streaming API가 존재한다. (이 둘 중 한 가지를 골라 서비스에 적용해야 하는데 이 부분은 책의 p.95~100을 보고 다시 정리해보려 한다.)

- **Spark Streaming**

    API와 커넥터의 집합으로, 스파크 프로그램이 일정 시간으로 간격을 두어 마이크로배치 형태로 스트림으로부터 수집된 작은 단위의 데이터를 받고, 주어진 계산을 수행하고, 매 간격 마다 결과를 반환한다.

- **Spark Structured Streaming**

    SQL 쿼리 최적화 장치인 카탈리스트에 구축된 API와 커넥터의 집합으로, 데이터프레임에 기반한 API와 스트림으로부터 발생하는 새로운 레코드로 인해 끊임없이 업데이트되는 무한한 테이블에 대한 연속적인 쿼리 개념을 제공한다.

### readStream

- 스트림이 수행할 프로세스를 정의한 것이다. 실제 데이터 처리는 이루어지지 않는다.

### writeStream

Stream consuming을 시작하고 쿼리에 선언된 계산을 구체화하여 결과를 지정된 출력 sink에 적재하는 Streaming Query를 반환한다.

Structured Streaming Job을 실행하기 위해서는 Sink 및 OutputMode를 지정해야 한다.

- Sink:
    - 결과 데이터를 어디에 어떠한 형식으로 저장할지 정의한다.
- OutputMode:
    - 결과 전달 방법을 정의한다. 크게 아래의 세 가지로 구분할 수 있다.
        1. 매번 모든 데이터를 볼 것인가?
        2. 오직 업데이트가 발생할 때만 볼 것인가?
        3. 새로운 레코드만 볼 것인가?

### Tutorial

------

- Code: Read Data From Kafka

    ### Read Data From Kafka with Spark

    spark.readStream을 사용하여 카프카의 어떤 토픽에서 데이터를 가져올지 결정한다.

    spark.readStream은 fluid API를 사용하여 스트리밍 소스를 구성하는데 필요한 정보를 수집하기 위해 빌더 패턴을 구현하는 클래스인 DataStreamReader를 반환한다.

    ```python
    kafka_broker_server = 'end_point'
    topic = 'topic'
    
    df = (spark.readStream
    		.format('kafka')
    		.option('kafka.bootsrap.servers', kafka_broker_server)
    		.option('subscribe', topic)
    		.option('startingOffsets', 'latest')
    		.load()) # DataStreamReader 객체를 평가하고 데이터프레임을 반환
    
    df.isStreaming # True
    ```

    ### Kafka Read Options

    | 옵션명                  | 설명                                                  |
    | ----------------------- | ----------------------------------------------------- |
    | kafka.bootstrap.servers | 카프카 서버                                           |
    | subscribe               | 카프카 토픽(구독할 주체)                              |
    | startingOffsets         | Streaming App이 새로 시작될 때 적용되는 오프셋 재설정 |

    ### Kafka의 고정된 반환 컬럼

    실제 보고자 하는 데이터는 value 컬럼에 존재, value를 제외한 나머지는 메타데이터로 보아도 무방하다.

    - key
    - value
    - topic
    - partition
    - offset
    - timestamp
    - timestampType

- Code: WriteStream to specific path

    ### writeStream

    구조적 스트리밍에서는 write 작업이 주용하다. 선언된 변환이 스트림에서 완료되었음을 표시하고 write 모드를 정의하며 start()를 호출하면 연속 쿼리에 대한 처리가 시작된다.

    구조적 스트리밍에서 모든 작업은 스트리밍 데이터로 수행하려는 작업에 대한 늦은 선언이다. start()를 호출할 때만 스트림의 실제 소비가 시작되고 데이터에 대한 쿼리 작업이 실제 결과로 구체화된다.

    ```python
    (df.writeStream
    		.outputMode('append')
    		.format('parquet')
    		.option('path', target_path)
    		.option('checkpointLocation', '/tmp/checkpoint')
    		.start()) # StreamingQuery 인스턴스가 반환된다.
    ```

    - writeStream은 유연한 인터페이스를 사용하여 원하는 write 작업에 대한 옵션을 구성할 수 있는 빌더 객체를 만든다.
    - format을 사용하여 결과 다운스트림을 구체화할 싱크를 지정한다. 위 예제의 경우 FileStreamSink와 파케이 형식을 사용한다.
    - `StreamingQueryInstance.recentProgress` : 실행 중인 StreamingQuery의 상태에 대한 정보를 요청하여 이를 출력한다.

- Console과 Memory에 Kafka 결과 출력

    카프카 데이터는 스키마를 확인할 순 있으나 데이터 자체를 `df.show()` 로 출력할 수 없다. 그 대신 console에 출력하는 형태로 값을 확인할 수 있다

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
    memory_sink = (df.writeStream
    		.queryName('kafka_memory')
    		.format('memory')
    		.start())
    
    spark.sql('SELECT * FROM kafka_memory').show()
    
    memory_sink.stop() # Stop streaming process
    ```

### References

------

https://spark.apache.org/docs/latest/api/python/reference/pyspark.streaming.html