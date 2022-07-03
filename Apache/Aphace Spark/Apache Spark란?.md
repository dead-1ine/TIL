# Apache Spark란?

- 대용량 데이터 프로세싱을 위한 빠르고 범용적인 인메모리 기반 클러스터 컴퓨팅 엔진
- 분산 메모리 기반의 빠른 분산 병렬 처리
- 배치, 대화형 쿼리, 스트리밍, 머신러닝과 같은 다양한 작업 타입을 지원하는 범용 엔진으로 Hadoop과 호환
- Scala, Java, Python, R 기반 High-level APIs 제공



# Apache Spark 특징

- In-Memory 컴퓨팅 (Disk 기반도 가능)
- RDD(Resilient Distributed Dataset) 데이터 모델
- Rich APIs 제공
- General execution graphs => DAG => Multiple stages of map & reduce
- Hadoop과의 유연한 연계 (HDFS, HBase, YARN and Others)
- 빠른 데이터 Processing(In-Memory Cached RDD)
- 실시간 Sream Processing
- 하나의 애플리케이션에서 배치, SQL 쿼리, 스트리밍, 머신러닝과 같은 다양한 작업을 하나의 워크플로우로 결합 가능
- Both fast to write and fast to run



# RDD (Resilient Distributed Dataset)

- Dataset

​		메모리나 디스크에 분산 저장된 변경 불가능한 데이터 객체들의 모음

- Distributed 

​		RDD에 있는 데이터는 클러스터에 자동 분배 및 병렬 연산 수행

- Resilient

​		클러스터의 한 노드가 실패하더라도 다른 노드가 작업 처리
​		(RDD Lineage, Automatically rebuilt on failure)

- Immutable

​		RDD는 수정이 안됨, 변형을 통한 새로운 RDD를 생성

- Operation APIs

    Transformations(데이터 변형, e.g. map, filter, groupBy, join)

    Actions(결과 연산 리턴/저장, e.g. count, collect, save)

- Lazy Evaluation

​		All Transformations (Action 실행 때까지)

- Controllable Persistence

​		Cache in RAM/Disk 가능(반복 연산에 유리)



# RDD 생성 -> RDD 변형 -> RDD 연산

Raw 데이터에서 여러 Transformation을 실행, 이후 Action을 통해 최종 Value를 만드는 연산을 수행