# Stream Processing

## Stream Processing이 중요한 이유

스트림 프로세싱은 금융 거래나 시장 및 통화 상태 모니터링, 보안 탐지나 시스템 실시간 분석과 같은 스트리밍 분석 또는 실시간 분석에 사용되는 기술이다. 일정량 또는 일정기간 동안 데이터를 모아서 한꺼번에 처리하는 배치 처리와 비교하여 연속되는 실시간 데이터를 처리하기 때문에 빠르고 효율적인 데이터 활용이 가능하다.



## Stream Processing이 무엇인가

스트리밍 데이터는 복수의 데이터 소스로부터 연속적으로 생성되는 데이터 레코드로 대부분 KB 단위 크기이다. 시냇물이 흐르듯 데이터가 연속해서 계속 흘러가기 때문에 처리할 수 있는 기회가 한정되고 처리할 수 없는 데이터는 버려질 수도 있다. 스트림 프로세싱은 스트리밍 데이터가 레코드나 정의된 단위에 따라 순차적으로 처리되는 것을 의미한다. 

이때 처리 과정은 단순 수집에서부터 합계, 평균 계산과 같은 집계와 패턴에 기반한 예측 분석 및 데이터 형식을 변환하거나 다른 데이터 소스와 결합 등을 수반한다.



## ESP, CEP

- ESP(Event Stream Processing)

    스트림 프로세싱과 동일한 의미로 사용된다.

    - 목적: 지속적으로 변화하는 이벤트를 빠르게 분석
    - 특징: 1990년대 DMBS 관련 회사를 중심으로 실시간 데이터 분석 목적으로 시작됨

- CEP(Complex Event Processing)

    스트림 프로세스와 유사하지만 분산 환경에서 발생하는 이벤트의 패턴을 분석한다는 점이 특징이다.

    - 목적: 다양한 이벤트로부터 패턴을 분석
    - 특징: 1980년대 분산 환경의 다양한 시스템에서 발생하는 이벤트 분석 목적으로 시작됨

    

## Stream Processing과 Batch Processing

스트림 프로세싱은 흔히 배치 프로세싱과 비교되거나 대안으로 제시된다. 하지만 스트림 프로세싱의 활성화가 모든 일괄 처리 작업을 대체하는 것은 아니다. 배치 프로세싱은 대규모 정적 데이터 세트를 대상으로 작업하는 경우에 알맞으며, 스트림 프로세싱은 동적으로 흘러가는 데이터 처리에 적합하다. 따라서 당연한 얘기지만 환경의 특성을 고려하여 아키텍처를 구성해야 한다. 두 방식은 상호 보완적으로 사용되며 이들을 결합한 하이브리드 모델도 존재한다. 예를 들면, 실시간 데이터를 실시간 프로세싱으로 처리한 후 누적된 데이터를 배치 프로세싱으로 작업하는 경우를 들 수 있다.

- Processing별 특징

| 기준      | Batch                                                        | Stream                                                       |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 처리 방식 | - 일정 기간 단위로 수집하여 한 번에 처리                     | - 연속된 데이터를 하나씩 처리                                |
| 처리량    | - 대규모 데이터 단위                                         | - 주로 소량의 레코드 단위                                    |
| 속도      | - 수 분 ~ 시간의 지연시간                                    | - (준)실시간                                                 |
| 사용환경  | - 복잡한 분석이 요구되는 환경<br />- 데이터 처리량이 많은 환경<br />- 데이터를 스트림으로 전달할 수 없는 레거시 시스템 환경 | - 실시간 처리 및 분석 정보가 요구되는 환경<br />- 고급 메시징 |
| 사용 예   | - 급여 및 청구 시스템                                        | - 은행 ATM<br />- 부정행위 탐지 및 모니터링 시스템<br />- SNS 데이터 분석 |



이와 같은 스트림 프로세싱의 특성은 이벤트 처리 보장, 내결함성 및 상태 관리 등을 통해 지원된다. 이벤트 처리 보장은 분산 데이터 파이프라인에서 데이터를 전달하는 방법으로 At-least-once, At-most-once, Exactly-once의 3가지로 나눌 수 있다. 이 중 Exactly-once가 가장 신뢰할 수 있는 방법이지만, 성능 부하로 인한 비요을 고려하여 3가지 중 적절한 방법을 택해야 한다.

- 데이터 전달 방법

| 방법          | 설명                                                         |
| ------------- | ------------------------------------------------------------ |
| At-least-once | - 최소 한 번의 전달 보장<br />- 데이터 전송 후 전달 완료가 확인되지 않아 타임아웃되면 재전송<br />- 데이터가 중복으로 수신되어도 무방한 경우에 사용 |
| At-most-once  | - 한 번의 전송만 수행<br />- 지연이나 유실이 발생해도 데이터를 재전송하지 않음<br />- 데이터를 수신하지 않아도 무방한 경우에 사용 |
| Exactly-once  | - 정확하게 한 번의 전달만 보장                               |



내결함성은 장애가 발생하면 복구하여 처리 시점부터 재개할 수 있는 기능이다. 일례로 Apache Flink의 경우 이벤트 스트림이 메모리에 적재되기 때문에 시스템이 갑작스럽게 중단되면 처리 중이던 데이터의 복구가 어려울 수 있다. 이를 방지하기 위해 SavePoint 기능으로 현재 메모리에 적재된 내용의 스냅샷을 영구 저장소에 백업하는 기능을 지원한다.

이벤트 처리는 입력 데이터의 가공과 분석을 수반하기도 하므로 현재 상태를 관리하고 갱신할 수 있어야 한다. 이를 위해 실시간으로 유입되는 데이터에 워터마크나 유한 크기로 분할해 처리하는 윈도우 개념이 적용되기도 한다.

스트림 프로세싱은 구현 방법에 따라 Native Stream과 Micro Batch 형태로 구분할 수 있다. 네이티브 스트림은 지속적으로 유입되는 새로운 데이터를 처리하기 위해 별도의 프로세서를 두기 때문에 상태 관리가 용이하다. 이 프로세서는 프레임워크에 따라 오퍼레이터, 태스크 등으로 불리며 데이터의 가공 처리를 수행할 수 있다. 소규모 일괄처리는 일반적인 배치처리와 비교하였을 때 작업 수행주기의 기간임계치가 짧다. 네이티브 스트림과 비교하면 상태관리는 어렵지만 내결함성 면에서 이점이 있다.

| 구현 방식     | 특성                                                         | 대표 제품                    |
| ------------- | ------------------------------------------------------------ | ---------------------------- |
| Native Stream | - 지연시간 최소<br />- 이벤트 처리 보장 방식에 따라 내결함성 유지가 어려움 | - Flink<br />- Kafka Streams |
| Micro Batch   | - 네이티브 스트림 대비 지연시간 발생                         | - Spark                      |



## 대표 Stream Processor

- Spark
- Storm
- Samza
- Kafka Streams
- Flink



### Apache Spark

UC버클리대학교에서 개발하였다. 스트림을 소규모 일괄처리하는 형태이기 때문에 Latency가 발생하지만 가장 활성화되어 있는 스트림 프로세서 중 하나로 **Exactly-once**의 이벤트 처리를 보장한다. 사용이 비교적 어렵지만 고급 분석 기능을 제공한다.

### Apache Storm

초창기 오픈소스 스트림 프로세싱 프레임워크 중 하나로 트위터에 의해 오픈소스화되었다. Latency가 매우 짧고 복잡하지 않은 스트림에 적합하다. 하지만, 소규모 일괄처리 스트림 모델인 Storm Trident를 사용하지 않으면 **At-least-once**의 이벤트 처리를 보장한다. 또한 상태 관리가 지원되지 않아 집계, 윈도우, 워터마크 등을 사용할 수 없기에 고급 분석에 제약이 있다.

### Apache Samza

삼자는 카프카를 만든 링크드인에서 개발되었으며, 카프카와 연동하는 환경에 적합한 스트림 프로세서이다. 하지만 카프카와 밀접하게 연관되어 있는 만큼 다른 제품과 연동이 어렵고 **At-least-once** 수준의 이벤트 처리를 보장한다.

### Apache Kafka Streams

카프카는 링크드인에서 개발하였다. 이후 링크드인에서 카프카를 개발한 엔지니어들이 Confluent를 창립해 지금까지 카프카를 발전시키고 있다. 카프카 스트림즈는 카프카 기능의 일부로, 스트림 프로세싱을 위한 경량 라이브러리이다. 스파크나 플링크보다 강력하진 않지만 **Exactly-once**의 이벤트 처리를 보장한다. 또한 다른 스트림 프로세서들이 실행 프레임워크인 것에 비해 사용이 쉽다는 이점이 있다.

### Apache Flink

플링크는 독일어로 민첩함을 뜻하는 단어로 베를린 TU대학교에서 시작된 프로젝트이다. **Exactly-once**의 이벤트 처리를 보장하는 네이티브 스트림 방식으로, Latency가 적고 처리량은 높으며 비교적 사용하기 쉬운 이점이 있다. 배치 처리 기능도 제공하지만 스트림 프로세싱을 주 목적으로 사용한다.

### 이 외의 프레임워크

- GCP Dataflow
- Apache Beam
- Akka Streams
- Apache NiFi
- Apache Apex
- Apaceh Pulsar
- Apache Twitter Heron