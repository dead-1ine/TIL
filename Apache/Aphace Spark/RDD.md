# RDD (Resillient Distributed Dataset)



## RDD 개념

RDD는 Resillient Distributed Dataset의 줄임말로 각 단어는 아래와 같은 뜻을 가진다.

- Resillient(회복력 있는, 변하지 않는): 메모리 내부에서 데이터 손실이 발생하면 유실된 파티션을 재연산해 복구
- Distributed(분산된): 스파크 클러스터를 통해 메모리에 분산하여 저장
- Dataset: 파일, 정보 등의 데이터

즉, "회복이 가능한 분산 데이터" 정도로 해석할 수 있다.



## RDD Lineage

RDD는 Lineage(사전적 의미로는 혈통)를 가진다.
RDD는 Read Only 특징을 가지는데, 이는 RDD 자체가 변환되는 것이 아닌 이전 RDD를 통해 새로운 RDD를 생성한다는 것이다. 그렇기에 스파크 내의 연산에 있어 그 수에 맞는 수 많은 RDD들이 생성되게 된다.
이 때 생성되는 연산 순서가 바로 "Lineage"이다.

특정 동작에 의해 생성되는 RDD Lineage는 DAG(Directed Acyclic Graph)의 형태를 가진다.
DAG의 특징은 각 노드 간의 순환이 없으며, 일정한 방향성만을 가지기 때문에 각 노드 간 의존성이 있으며 그 순서가 중요하다.

이러한 DAG에 의해 특정 RDD 관련 정보가 메모리에서 유실되었을 경우 Graph를 복기하여 다시 계산하고 유실된 RDD(데이터)를 복구할 수 있다.

스파크의 이러한 특성 때문에 "Fault-tolerant"(작업 중 장애나 고장이 발생하여도 예비 부품이나 절차가 즉시 그 역할을 대체 수행하므로 서비스의 중단이 없게 하는 특성)를 보장하는 강력한 기능을 가진다.



## RDD 동작원리



참고 블로그: https://artist-developer.tistory.com/17