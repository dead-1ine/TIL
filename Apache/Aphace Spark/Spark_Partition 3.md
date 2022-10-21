- artition은 RDD나 Dataset을 구성하고 있는 최소 단위 객체이다.
- 각 Partition은 서로 다른 노드에서 분산 처리된다.

- Spark에서는 하나의 최소 연산을 Task라고 표현하는데, 이 하나의 Task에서 하나의 Partition이 처리된다. 또한, 하나의 Task는 하나의 Core가 연산을 처리한다.
- **1 Core == 1 Task == 1 Partition**

- 이처럼 설정된 Partition 수에 따라 각 Partition의 크기가 결정된다.
- 그리고 이 Partition의 크기가 결국 Core 당 필요한 메모리 크기를 결정한다.
	- Partition 수 -> Core 수
	- Partition 크기 -> 메모리 크기

- 따라서, Partition의 크기와 수가 Spark 성능에 큰 영향을 미치는데, 통상적으로 Partition의 크기가 클 수록 메모리가 더 필요하고, Partition의 수가 많을수록 Core가 더 필요하다.
	- 적은 수의 Partition == 크기가 큰 Partition
	- 많은 수의 Partition == 크기가 작은 Partition

- 즉, Partition의 수를 늘리는 것은 Task 당 필요한 메모리를 줄이고 병렬화의 정도를 늘린다.

# Spark Partition의 종류
---
> 동일한 Partition이지만 쓰이는 때에 따라 다음과 같은 3가지로 구분지을 수 있다.
	- Input Partition
	- Output Partition
	- Shuffle Partition

- 이 중, Spark의 주요 연산이 Shuffle인 만큼, Shuffle Partition이 가장 중요하다.

## Input Partition
관련 설정: spark.sql.files.maxpartitionBytes

Input Partition은 처음 파일을 읽을 때 생성하는 Partition이다.
관련 설정값은 위와 같으며 Input Partition의 크기를 설정할 수 있고, 기본 값은 128MB이다.

- 파일(HDFS 상의 마지막 경로에 존재하는 파일)의 크기가 128MB보다 크면 Spark에서 128MB만큼 쪼개면서 파일을 읽는다.
- 파일의 크기가 128MB보다 작다면 그대로 읽어 들여 파일 하나당 Partition 하나가 된다.

대부분의 경우 필요한 컬럼만 뽑아 사용하기 때문에 파일은 128MB보다 작다. 가끔 큰 파일을 다룰 경우 이 설정값을 조절해야 한다.

- Use Case
	- 파일 하나의 크기가 매우 크고 수도 많다면 설정값의 크기를 늘리고 자원도 늘려야 하지만 이런 경우는 잘 없다고 한다.
	- 또한, 필요한 컬럼만 사용하기 때문에 데이터의 크기는 더 작아진다.

Output Partition
	파일을 저장할 때 생성하는 partition
	기본적으로 HDFS는 큰 파일을 다루도록 설계되어 있어 크기가 큰 파일로 저장하는 것이 좋다.
	일반적으로 HDFS Blocksize에 맞게 설정한다. 
	아래는 AWS EMR의 기본 HDFS Blocksize이다

출처: https://tech.kakao.com/2021/10/08/spark-shuffle-partition/