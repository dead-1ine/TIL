데이터 파이프라인에 필요한 기술
프로그래밍 능력
데이터 분석 능력(쿼리)
시각화 기술
소통 능력(협업 with 데이터 분석가, 사이언티스트, 개발자 등)
도메인에 대한 깊은 이해



# 용어 정리

---

### Batch

데이터를 실시간으로 처리하는 것이 아니라, 일괄적으로 모아서 처리하는 작업을 말한다. 예를 들어 하루종일 쌓인 데이터를 Batch Job을 통해 특정 시간에 한꺼번에 처리하는 경우가 있다.



### Batch Processing

일괄처리라고도 하며, 실시간으로 요청에 의해 처리되는 방식이 아닌 일괄적으로 한꺼번에 대량의 프로세스를 처리하는 방식이다.



### Pod

작업이 시작되면 항상 실행되는 것을 의미한다.



### Job

-   하나 이상의 Pod를 지정하고 지정된 수의 Pod를 성공적으로 실행하도록 하는 설정이다. 
-   백업이나 특정 배치 파일들처럼 한 번 실행하고 종료되는 성격의 작업에서 사용될 수 있다.



### CronJob

-   지정한 일정에 따라 Job을 실행시킬 수 있다.
-   예를 들어, 매일 오후 5시에 특정 Pod를 실행한다.



### Bulk

-   DW에서 사용하는 형태로, 이미 DB나 파일 서버 등에서 각각의 방식으로 데이터를 추출할 때 이 방식을 사용한다.



###  Streaming

-   실시간성으로 마치 흐르는 물처럼 데이터가 끊임없이 흘러들어오는 것을 수집하는 것이다.



### Message Delivery

-   IoT처럼 다수의 클라이언트가 계속해서 작은 데이터를 전송하는 방식이다.
-   보통 2가지 방법으로 Message Delivery 데이터를 저장한다.
    1.   NoSQL에 저장
    2.   Message Broker사용
-   Message Broker의 대표적인 예는 Apache Kafka이다.
-   Message Broker는 NoSQL에서 발생할 수 있는 다수의 작은 데이터가 계속 저장될 때 쓰기 성능의 한계를 방지하기 위해 중간에 일종의 완충제 역할을 하게 한다.