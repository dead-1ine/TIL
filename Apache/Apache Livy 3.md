# Apache Livy

Livy는 REST API를 통해 Spark 작업을 요청할 수 있는 서비스이다. REST API와 Java, Scala 라이브러리를 이용해 작업을 요청할 수 있다.

Livy의 특징은 아래와 같다.

- 멀티 클라이언트에서 여러 개의 Spark 작업을 요청할 수 있다.
- 작업 간 RDD와 데이터프레임 공유가 가능하다.
- 여러 개의 Spark Context를 관리할 수 있고, Spark Context는 YARN이나 Mesos와 같은 클러스터에서 실행된다.(Livy 서버에서 실행되지 않음)
- Spark 작업은 JAR, Java/Scala, 코드 조각을 통해 요청한다.
- 보안 통신을 이용해 안정성을 제공한다.



### REST API Request Format

```python
# POST 방식으로 작업 실행
# curl 옵션
# 	-X: 전송방식
# 	-H: 헤더 정보 추가
# 	-d: POST 파라미터(JSON 형식)
# file: jar
# queue: YARN 큐네임
# className: 실행 클래스
# args: 실행 인자
```



### 예시

```python
curl -X POST \
-H "Content-Type:application/json" \
-d "{
	file: "hdfs://0.0.0.0:8020/sample.jar",
	queue: "queue_name",
    className: "sdk.test.SparkSample",
    args: [A, B]
}" \
http://$(hostname- f):8998/batches
```

