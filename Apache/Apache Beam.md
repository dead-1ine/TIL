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



Beam은 Functional Programming 패러다임에 따라 디자인되었다. 따라서 loop 대신 PCollection 내의 각 데이터 처리를 위해 PTransform 함수를 연결해 사용할 수 있다. (파이프라인 내에서 'abc' >> 와 같은 형태로 comment를 사용할 수 있다.)

```python
import apache_beam as beam

inputs = [0, 1, 2, 3]

with beam.Pipeline() as pipeline:
    outputs = (
    	pipeline
        | 'Create values' >> beam.Create(inputs)
        | 'Multiply by 2' >> beam.Map(lambda x: x * 2)
    )
    
    outputs | beam.Map(print)
```



## Windowing

Windowing은 PCollection을 타임스탬프나 어떤 기준 요소로 잘라서 보는 것을 말한다. 어떤 PCollection을 논리적 윈도우로 잘라볼 수 있다. 각 요소들은 하나 혹은 그 이상의 윈도우에 속해서 GroupByKey 또는 Combine 등의 Aggregation 연산 등에 활용될 수 있다.

Windowing의 방식은 세 가지가 있다.

1. Fixed Time Windows
2. Sliding Time Windows
3. Session Windows



### 1. Fixed Time Windows

가장 기본적인 형태의 윈도우로, 지정된 타임스탬프 단위의 고정된 시간으로 윈도우를 잘라내는 형태로 활용한다.

- 30초 단위의 Fixed Window를 설정하는 코드

```python
from apache_beam import beam, window

fixed_windowed_itmes = (
    itmes | 'window' >> beam.WindowInto(window.FixedWindows(60))
)
```



### 2. Sliding Time Windows

타임스탬프 등의 시간 기준으로 데이터 스트림을 잘라내는데 윈도우간 겹침이 가능하다. 윈도우의 길이는 duration이라고 하며, 각 윈도우가 시작되는 부분을 period라고 한다.



### 3. Session Windows

세션 윈도우는 윈도우 사이에 갭이 생길 수 있는 데이터의 형태에 활용할 수 있다. 정해진 Minimum gap duration보다 작은 간격을 두고 들어온 데이터는 동일한 윈도우로 처리한다. 클릭스트림 로그 ,유저 로그 등에서 유저별로 세션을 만들어서 기록할 때 활용할 수 있다.



## Watermark & Late Data

워터마크는 스트리밍 처리 시 늦게 도착하는 데이터의 이슈를 풀기 위한 재밌는 컨셉이다. 특정 타임스탬프 안에 들어오는 데이터를 윈도우에 넣는 형태로 데이터를 프로세싱할 때 네트워크, 클라이언트 등의 이슈로 데이터가 지연 도착하는 경우가 발생할 수 있다. 지연이 심해지면 원래의 해당 데이터가 속해야 할 윈도우의 데이터 프로세싱이 끝난 이후 도착하는 경우도 있을 수 있다. (12:30:00에 윈도우가 종료되었는데 12:29:59 타임스탬프 데이터가 12:31:00에 도착한 경우)

이런 데이터의 처리를 위해 Beam에서는 Watermark라는 기능을 제공한다. 윈도우가 종료된 이후에도 계속 데이터가 들어오면 Watermark를 뒤로 미루는 식으로 다이나믹하게 Watermark를 설정할 수 있다. Watermark 내에 들어오는 데이터는 지연도착으로 분류되지 않고 같은 윈도우 내에 속할 수 있게 된다. 

- Watermark: 워터마크 타임스탬프가 지정된 시간을 지나면, 시스템은 이보다 늦게 들어오는 데이터는 없을 거시라 인식한다. 즉 마지막 지각생까지 처리가 되었다고 가정한다. 그 이후에 들어오는 데이터는 설정에 따라 버려지거나 지연처리하게 된다.
- Late Data: 워터마크 이후에 들어오는 데이터이다.

Beam의 디폴트 설정은 윈도우의 끝 지점과 워터마크 지점이 동일하기 때문에, Late Data를 허용하지 않는다.

- Late Data 허용 Example

```python
pc = [Initial PCollection]

pc | beam.WindowInto(
	FixedWindows(60),
    trigger = trigger_fn,
    accumulation_mode = accumulation_mode,
    timestamp_combiner = timestamp_combiner,
    allowed_lateness = Duration(seconds=2*24*60*60) # 2 days
)
```



## Trigger

스트리밍 처리된 데이터를 윈도우로 그룹핑하기 위한 기준을 트리거라고 한다. PCollection의 트리거 기준은 자유롭게 설정할 수 있다.

아래는 기본적인 pre-built 트리거이다.

- Event time triggers
    Beam의 디폴트 트리거, 데이터의 타임스탬프 기준으로 윈도우를 그룹핑
- Processing time triggers
    파이프라인 내의 프로세싱 타임 기준 트리거
- Data-driven triggers
    윈도우 내 데이터를 체크하여 트리거. 현재는 데이터 개수 기준 트리거링만 제공
- Composite tirggers
    몇 가지 트리거를 조합해서 생성한 트리거



## Beam의 장단점

Beam이 Spark나 Flink와 비교했을 때 더 나은 점이 뭘까.

---

출처: https://jaemunbro.medium.com/gcp-dataflow-apache-beam-알아보기-a4f5f09b98d1