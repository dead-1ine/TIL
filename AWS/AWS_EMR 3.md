# Amazon EMR

Amazon EMR은 Apache Spark, Apache Hive 및 Presto와 같은 오픈소스 분석 프레임워크를 사용하여 대규모 분산 데이터 처리 작업, 대화형 SQL 쿼리 및 ML 애플리케이션을 실행하기 위한 클라우드 빅 데이터 플랫폼이다.

"Amazon EC2 Instance를 이용해 하둡, 스파크 클러스터를 몇 분만에 생성할 수 있다."

# 사용 사례

- 빅데이터 분석 수행
- 확장 가능한 데이터 파이프라인 구축

- 실시간 데이터 스트림 처리
- 데이터 과학 및 ML 채택 가속화



## Apache Hadoop on EMR

> 일반적으로 이야기하는 Hadoop은 MapReduce, YARN, HDFS를 통칭한다.

  EMR은 EC2 instance Cluster를 이용해 하둡 프레임워크를 실행할 수 있다. 하둡 에코시스템에 속한 Hive, Pig, Hue, Ganglia, Ozzie, HBase 등 다양한 어플리엨이션 또한 EMR 위에서 사용이 가능하다.
  Amazon EMR은 Storage로 사용될 S3와 연결시켜주는 EMRFS(EMR File System)를 지원한다.



## Processing with Hadoop MapReduce, Tez and YARN

  MapReduce와 Tez는 하둡 에코시스템에서 실행엔진으로 동작하는데, Job을 여러 작은 조각으로 나누어 Amazone EMR Cluster에 분배하여 분산처리한다. Cluster에 있는 어떠한 노드가 중간에 작업에 실패하더라도 계속 작업 가능하도록 Fault-tolerance가 적용되어 있다.
  Hadoop2가 나오면서 EMR Cluster의 리소스는 YARN을 통해 관리된다. YARN은 Cluster에 있는 리소스를 관리하고 Job이 잘 실행될 수 있도록 감시한다.



## Storage using Amazon S3 and EMRFS(EMR File System)

  EMRFS를 이용하면 S3를 데이터 저장소로 사용할 수 있다. S3는 HDFS API를 만족하며, 용량 또한 무한이기에 대용량 처리에 적합하다. 데이터와 처리를 같이하는 HDFS와 달리 EMR과 S3를 따로 두는 이유는 실행 레이어와 스토리지 레이어를 분리하기 위함이다. 예를 들어, 분산처리가 실행되지 않을 경우에는 EMR Cluster의 규모를 줄일 수 있다.



## On-cluster storage with HDFS

  Amazon EMR Cluster에는 HDFS가 설치되어 있다. 따라서 S3와 같이 EMR Cluster의 HDFS 또한 데이터 저장소로 사용할 수 있다. Cluster의 HDFS는 주로 분산처리 도중 생성되는 중간 결과물들을 데이터로 저장하기 위해 사용된다. 최종 결과나 인풋 데이터들은 S3에 위치할 것이다.