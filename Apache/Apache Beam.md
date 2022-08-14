# Apache Beam

Beam은 batch 혹은 stream으로 주어지는 데이터에 대해 효율적인 병렬처리를 지원하는 파이프라인 모델이다. Beam SDK를 활용해 파이프라인을 만들면 여러 개의 Runner에서 이를 효율적으로 실행할 수 있게 한다.

Beak SDK는 Java, Python, Go의 세 언어로 제공되며, Portability SDK를 통해 다른 언어로 기술되어 있는 파이프라인 Op를 가져와 사용할 수도 있다.

Runner는 Beam 파이프라인을 실행할 수 있는 일종의 Back-end로, 보통 분산 처리를 지원하는 시스템에서 사용한다. 대표적인 Runner는 아래와 같다.

- Direct Runner
    - 파이프라인을 로컬 환경에서 실행한다. 보통 디버깅 목적으로 사용한다.
- Portable Runner
    - 파이프라인을 컨테이너 환경에서 실행한다.
- Google Cloud Dataflow Runner
    - 대표적인 Apache Beam의 Managed Service이다.

이 외에도 Flink, Spark, Samze, Nemo, Hazelcast Jet Runner, Twister2 Runner 등 다양한 종류의 Runner가 있다.



## 장점

가장 큰 장점은 매우 큰 크기의 데이터를 병렬로 쪼개어 효율적으로 처리할 수 있다는 점이다. Beam 파이프라인은 입력으로 들어온 데이터를 작은 처리 단위로 나누고, 수 많은 Worker들에게 각 처리 단위를 분배하여 분산 처리하는 방식을 사용한다. 그러면서도 매우 직관적인 프로그래밍 인터페이스를 제공하기 때문에 쉽고 빠르게 파이프라인을 구축해서 실행햅로 수 있다.

Direct Runner를 사용해 로컬 환경에서 디버깅해볼 수도 있다는 점도 큰 장점이다. 여러 개의 Container를 기반으로 만들어지거나 DAG가 실행 환경에 강하게 엮인 파이프라인 프레임워크들은 디버깅을 위해 테스트 환경을 별도로 만들어야 하는 경우가 많은데, Beam은 그럴 필요 없이 외부로 향하는 I/O 부분만 잘 처리해준다면 로컬에서 모든 과정을 쉽게 실행해볼 수 있다.

대부분의 데이터 파이프라인에 잘 어울리기 때문에 간단한 ETL 작업부터 실시간 로그 정제 파이프라인까지 다양한 작업에 사용할 수 있다. 



## 사용 용도

### 데이터셋 정제 파이프라인

모델 학습을 위해 데이터를 정제할 때 봍오 큰 코퍼스를 읽어와 여러가지 처리를 한 후 데이터셋의 형태로 만들어 저장한다. Beam은 이 과정을 매우 직관적으로 프로그래밍할 수 있도록 지원하고, 동시에 매우 많은 수의 Worker를 통해 병렬로 실행할 수 있다.

GCP의 DataFlow Runner와 같이 사용할 수 있는데, DataFlow는 순식간에 몇 백대의 Worker를 만들어 데이터를 분배 후 처리하도록 명령할 수 있다. 또한 이 과정에서 데이터 처리 인프라나 클러스터 유지 관리 같은 것에 신경쓰지 않아도 된다는 점도 매우 큰 장점이다.



## Objects of Beam

Beam의 데이터 파이프라인을 구성하는 두 가지 주요 오브젝트는 Pcollections와 PTransformation이다.

- PCollections
    Beam의 파이프라인 안의 모든 데이터는 PCollection 안에 산다. (PCollection == Parallel Collection)
    PCollection은 분산 데이터셋이며, Immutable한 속성을 가진다.
- PTransforamtion
    데이터를 트랜스포메이션하는 작업은 PTransformations(Parallel Transformation)라는 function을 통해 진행된다. input으로 PCollections를 받고 변형하여 PCollections Output을 리턴한다.



### Pardo

Pardo는 Beam의 가장 일반적인 parallel processing transformation이다. Pardo는 분산처리 트랜스포메이션의 Map - Shuffle - Reduce 단계 중 Map에 가깝다. 

아래와 같은 일반적인 데이터 프로세싱 연산에 모두 사용된다.

- Filtering a dataset
- Formatting or type-converting each element in a dataset
- Extracting parts of each element in a dataset
- Performing computations on each element in a dataset

아래는 Pardo를 실행하기 위한 Sample Snippet이다.(Beam에서 파이프라인 내 스텝의 연결을 위한 delimiter는 파이프(|)를 사용한다.)

```python
# The input PCollection of Strings.
words = ...

# The DoFn to perform on each element in the input PCollection.

class ComputeWordLengthFn(beam.DoFn):
    def process(self, element):
        return [len(element)]
    
# Apply a Pardo to the PCollection "words" to compute lengths for each word.
word_lengths = words | beam.ParDo(ComputeWordLengthFn())
```



