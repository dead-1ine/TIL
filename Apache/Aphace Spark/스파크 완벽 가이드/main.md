[DataFrame](https://www.notion.so/DataFrame-e9acd4feebec4c32942d008d3dea80b5)

[Partition](https://www.notion.so/Partition-f62d818d56a74ccab5bf78c686b8a73a)

[Transformation](https://www.notion.so/Transformation-4988dc5000c04091ac6aa7703fd42730)

[NOTEs](https://www.notion.so/NOTEs-de07a371ddd447888151e86b85523860)

### Transformation

------

스파크의 핵심 데이터 구조는 불변성을 가진다. 즉, 한번 생성하면 변경할 수 없다. DataFrame을 변경하려면 원하는 변경 방법을 스파크에 알려줘야 한다. 이 때 사용하는 명령을 트랜스포메이션이라고 한다.

```python
divis_by2 = df.where('number % 2 = 0')
```

위 코드를 실행해도 추상적인 트랜스포메이션만 지정한 상태이기 때문에 액션을 호출하지 않으면 스파크는 실제 트랜스포메이션을 수행하지 않는다.

### Transformation Dependency

------

트랜스포메이션은 스파크에서 비즈니스 로직을 표현하는 핵심 개념이며, 두 가지 유형이 존재한다. 하나는 좁은 의존성(narrow dependency)이고 다른 하나는 넓은 의존성(wide dependency)이다.

좁은 의존성을 가진 트랜스포메이션은 각 입력 파티션이 하나의 출력 파티션에만 영향을 미친다. 위 예제의 `where` 구문은 좁은 의존성을 가진다. 따라서 하나의 파티션이 하나의 출력 파티션에만 영향을 미친다.

넓은 의존성을 가진 트랜스포메이션은 하나의 입력 파티션이 여러 출력 파티션에 영향을 미친다. 스파크가 클러스터에서 파티션을 교환하는 셔플이라는 단어를 자주 들었을 것이다. 좁은 트랜스포미메이션을 사용하면 스파크에서 파이프라이닝을 자동으로 수행한다. 즉,  DataFrame에 여러 필터를 지정하는 경우 모든 작업이 메모리에서 발생한다. 하지만 셔플은 다른 방식으로 동작한다. 스파크는 셔플의 결과를 디스크에 저장한다.

### Lazy Evaluation

------

지연 연산은 스파크가 연산 그래프를 처리하기 직전까지 기다리는 동작 방식을 의미한다. 스파크는 특정 연산 명령이 내려진 즉시 데이터를 수정하지 않고 원시 데이터에 적용할 트랜스포메이션의 실행 계획을 생성한다. 스파크는 코드를 실행하는 마지막 순간까지 대기하다가 원형 DataFrame 트랜스포메이션을 간결한 물리적 실행 계획으로 컴파일한다. 스파크는 이 과정을 거치며 전체 데이터 흐름을 최적화하는 엄청난 강점을 가지고 있다. DataFrame의 조건절 푸시다운(predicate pushdown)이 한 예가 될 수 있다. 아주 복잡한 스파크 작업이 원시 데이터에서 하나의 로우만 가져오는 필터를 가지고 있다면 필요한 레코드 하나만 읽는 것이 가장 효율적이다. 스파크는 이 필터를 데이터소스로 위임하는 최적화 작업을 자동으로 수행한다.

### Action

------

사용자는 트랜스포메이션을 사용해 논리적 실행 계획을 세울 수 있다. 하지만 실제 연산을 수행하려면 액션 명령을 내려야 한다. 액션은 일련의 트랜스포메이션으로부터 결과를 계산하도록 지시하는 명령이다.

count는 가장 단순한 액션이며 이 외에도 세 가지 유형의 액션이 있다.

- 콘솔에서 데이터를 보는 액션
- 각 언어로 된 네이티브 객체에 데이터를 모으는 액션
- 출력 데이터소스에 저장하는 액션

액션을 지정하면 스파크 잡이 시작된다.

### Spark UI

------

스파크 UI는 스파크 잡의 진행 상황을 모니터링할 때 사용한다. 스파크 UI에서는 스파크 잡의 상태, 환경 설정, 클러스터 상태 등의 정보를 확인할 수 있다. 스파크 UI는 잡을 튜닝하고 디버깅할 때 매우 유용하다.

### Explain()

------

DataFrame 객체에 explain()을 호출하면 DataFrame의 lineage나 스파크의 쿼리 실행 계획을 확인할 수 있다.

```python
flightData2015.sort('count').explain()

== Physical Plan ==
*Sort [count#195 ASC NULLS FIRST], true, 0
+- Exchange rangepartitioning(count#195 ASC NULLS FIRST, 200)
	+- *FileScan csv [DEST_COUNTRY_NAME#193,ORIGIN_COUNTRY_NAME#194,count#195]...
```

실행 계획은 위에서 아래 방향으로 읽으며 최종 결과는 가장 위에, 데이터 소스는 가장 아래에 있다.

explain()가 출력하는 실제 실행 계획은 물리적인 실행 시점에서 수행하는 최적화이다. 실행 계획은 트랜스포메이션의 지향성 비순환 그래프(directed acyclic graph, DAG)이며 액션이 호출되면 결과를 만든다. DAG의 각 단계는 불변성을 가진 신규 DataFrame을 생성한다.

```python
(flightData2015
		.groupby('DEST_COUNTRY_NAME')
		.sum('count')
		.withColumn('destination_total', col('sum(count)'))
		.sort(desc('destination_total')
		.limit(5)
		.explain()
)
== Physical Plan ==
TakeOrderedAndProject(limit=5, orderBy=[destination_total#16194L DESC], outpu...
+- *HashAggregate(keys=[DEST_COUNTRY_NAME#7323, 5), functions=[sum(count#7325L)])
		+- Exchange hashpartitioning(DEST_COUNTRY_NAME#7323, 5)
				+- *HashAggregate(keys=[DEST_COUNTRY_NAME#7323], functions=[partitial_sum...
						+- InMemoryTableScan [DEST_COUNTRY_NAME#7323, count#7325L]
								+- InMemoryRelation [DEST_COUNTRY_NAME#7323, ORIGIN_COUNTRY_NAME...
										+- *Scan csv [DEST_COUNTRY_NAME#7578,ORIGIN_COUNTRY_NAME...
```

### spark-submit

------

spark-submit 명령은 애플리케이션 코드를 클러스터에 전송해 실행시키는 역할을 한다. 클러스터에 제출된 애플리케이션은 작업이 종료되거나 에러가 발생할 때까지 실행된다.

spark-submit 명령에 애플리케이션 실행에 필요한 자원과 실행 방식 그리고 다양한 옵션을 지정할 수  있다.

- spark-submit 예제

    ```
    ./spark-submit \\
    	--master local \\
    	./examples/src/main/python/pi.py 10
    ```

spark-submit 명령 중 master 옵션의 인숫값을 변경하면 스파크가 지원하는 스파크 스탠드얼론, 메소스 그리고 YARN 클러스터 매니저에서 동일한 애플리케이션을 실행할 수 있다.

### Dataset

------

Dataset은 자바와 스칼라의 정적 데이터 타이베 맞는 코드, 즉 정적 타입 코드를 지원하기 위해 고안도니 스파크의 구조적 API이다. Dataset은 타입 안정성을 지원하며 동적 타입 언어인 파이썬과 R에서는 사용할 수 없다.

Dataset API는 DataFrame의 레코드를 사용자가 자바나 스칼라로 정의한 클래스에 할당하고 자바의 ArrayList 또는 스칼라의 Seq 객체 등의 고정 타입형 컬렉션으로 다룰 수 있는 기능을 제공한다. Dataset API는 타입 안정성을 지원하므로 초기화에 사용한 클래스 대신 다른 클래스를 사용해 접근할 수 없다. 따라서 Dataset API는 다수의 소프트웨어 엔지니어가 잘 정의된 인터페이스로 상호작용하는 대규모 애플리케이션을 개발하는 데 특히 유용하다.

Dataset 클래스는 내부 객체의 데이터 타입을 매개변수로 사용한다.

- 타입 안정성 함수와 DataFrame을 사용해 비즈니스 로직을 신속하게 작성하는 예제

    ```scala
    case class Flight(
    	DEST_COUNTRY_NAME: String,
    	ORIGIN_COUNTRY_NAME: String,
    	count: BigInt)
    
    val flightDF = spark.read
    	.parquet("/data/flight.paruqet/")
    
    val flights = flightsDF.as[Flight] //  DataFrame -> Dataset
    ```

Dataset의 장점은 collect()나 take()를 호출하면 DataFrame을 구성하는 Row 타입의 객체가 아닌 Dataset에 매개변수로 지정한 타입의 객체를 반환한다. 따라서 코드 변경 없이 타입 안정성을 보장할 수 잇으며 로컬이나 분산 클러스터 환경에서 데이터를 안전하게 다룰 수 있다.

### 저수준 API

------

스파크는 RDD를 통해 자바와 파이썬 객체를 다루는 데 필요한 다양한 기본 기능을 제공한다. 그리고 스파크의 거의 모든 기능은 RDD를 기반으로 만들어졌다. DataFrame 연산도 RDD를 기반으로 만들어졌으며 편리하고 매우 효율적인 분산 처리를 위해 저수준 명령으로 컴파일된다. 원시 데이터를 읽거나 다루는 용도로 RDD를 사용할 수 있지만 대부분의 경우는 구조적 API를 사용하는 것이 좋다. RDD를 이용해 파티션과 같은 물리적 실행 특성을 결정할 수 있으므로 DataFrame보다 더 세밀한 제어를 할 수 있다.

드라이버 시스템의 메모리에 저장된 원시 데이터를 병렬처리하는 데 RDD를 사용할 수 있다.

```scala
// Scala
spark.sparkContext.parallelize(Seq(1, 2, 3)).toDF()
# Python
from pyspark.sql import Row

spark.sparkContext.parallelize([Row(1), Row(2), Row(3)]).toDF()
```

RDD는 스칼라뿐만 아니라 파이썬에서도 사용할 수 있지만 두 언어의 RDD가 동일하지는 않다. 언어와 관계없이 동일한 실행특성을 제공하는 DataFrame API와는 다르게 RDD는 세부 구현 방식에서 차이를 보인다.

낮은 버전의 스파크 코드를 계속 사용해야 하는 상황이 아니라면 RDD를 사용해 스파크 코드를 작성할 필요는 없다. 최신 버전의 스파크에서는 기본적으로 RDD를 사용하지 않지만, 비정형 데이터나 정제되지 않은 원시 데이터를 처리해야 한다면 RDD를 사용해야 한다.

### DataFrame과 Dataset

------

DataFrame과 Dataset은 잘 정의된 로우와 컬럼을 가지는 분산 테이블 형태의 컬렉션이다. 각 컬럼은 다른 컬럼과 동일한 수의 로우를 가져야 하며 컬렉션의 모든 로우는 같은 데이터 타입 정보를 가져야 한다. DataFrame과 Dataset은 결과를 생성하기 위해 어떤 데이터에 어떤 연산을 적용해야 하는지 정의하는 지연 연산의 실행 계획이며, 불변성을 가진다. DataFrame에 액션을 호출하면 스파크는 트랜스포메이션을 실제로 실행하고 결과를 반환한다.

DataFrame과 Dataset을 조금 더 구체적으로 정의하려면 ‘스키마’에 대해 알아야 한다. 스키마는 분산 컬렉션에 저장할 데이터 타입을 정의하는 방법이다.

### Schema

------

스키마는 DataFrame의 컬럼명과 데이터 타입을 정의한다. 스키마는 데이터소스에서 얻거나(Schema-on-read) 직접 정의할 수 있다.

스키마는 여러 개의 StructField 타입으로 구성된 StructType 객체이다. StructField는 이름, 데이터 타입, nullable을 지정하는 불리언 값을 가진다. 필요한 경우 컬럼과 관련된 메타데이터를 지정할 수도 있다. 메타데이터는 해당 컬럼과 관련된 정보이며 스파크의 머신러닝 라이브러리에서 사용한다.

스키마는 복합 데이터 타입인 StructType을 가질 수 있다.

스파크는 런타임에 데이터 타입이 스키마의 데이터 타입과 일치하지 않으면 오류를 발생시킨다.

- 스키마를 정의하고 DataFrame에 적용하는 예제

    ```python
    import pyspark.sql.types import (
    		StructField, 
    		StructType, 
    		StringType, 
    		LongType)
    
    my_manual_schema = StructType([
    		StructField('DEST_COUNTRY_NAME', StringType(), True),
    		StructField('ORIGIN_COUNTRY_NAME', StringType(), True),
    		StructField('count', LongType(), False, metadata={'hello': 'world'})
    ])
    
    df = (spark.read
    		.format('json')
    		.schema(my_manual_schema)
    		.load('/data/flight-data/json/2015-summary.json')
    )
    ```

스파크는 자체 데이터 타입 정보를 사용하므로 프로그래밍 언어의 데이터 타입을 스파크의 데이터 타입으로 설정할 수 없다.

### 스파크의 구조적 데이터 타입 개요

------

스파크는 실행 계획 수립과 처리에 사용하는 자체 데이터 타입 정보를 가지는 카탈리스트 엔진을 사용한다. 카탈리스트 엔진은 다양한 실행 최적화 기능을 제공한다.

### DataFrame과 Dataset 비교

------

구조적 API에는 ‘비타입형’인 DataFrame과 ‘타입형’인 Dataset이 있다. 물론 DataFrame에도 데이터 타입이 있다. 하지만 스키마에 명시된 데이터 타입의 일치 여부를 런타임이 되어서야 확인이 가능하다. 반면 Dataset은 스키마에 명시된 데이터 타입의 일치 여부를 컴파일 타임에 확인한다. Dataset은 JVM 기반의 언어인 스칼라와 자바에서만 지원하며 Dataset의 데이터 타입을 정의하려면 스칼라의 case class나 자바 빈을 사용해야 한다.

스파크의 DataFrame은 Row 타입으로 구성된 Dataset이다. Row 타입은 스파크가 사용하는 ‘연산에 최적화된 인메모리 포맷’의 내부적 표현 방식이다. Row 타입을 사용하면 가비지 컬렉션과 객체 초기화 부하가 있는 JVM 데이터 타입을 사용하는 대신 자체 데이터 포맷을 사용하기 때문에 매우 효율적인 연산이 가능하다.

DataFrame을 사용하면 스파크의 최적화된 내부 포맷을 사용할 수 있다.

### Column

------

컬럼은 정수형이나 문자열 같은 **단순 데이터 타입**, 배열이나 맵 같은 **복합 데이터** 타입 그리고 **null**을 표현한다.

사용자는 표현식으로 DataFrame의 컬럼을 선택, 조작, 제거할 수 있다.

스파크의 컬럼은 표현식을 사용해 레코드 단위로 계산한 값을 단순하게 나타내는 논리적인 구조이다. 따라서 컬럼의 실제값을 얻으려면 로우가 필요하고, 로우를 얻으려면 DataFrame이 필요하다. DataFrame을 통하지 않으면 외부에서 컬럼에 접근할 수 없다. 컬럼 내용을 수정하려면 반드시 DataFrame의 트랜스포메이션을 사용해야 한다.

### Row

------

로우는 데이터 레코드이다. DataFrame의 레코드는 Row 타입으로 구성된다. 로우는 SQL, RDD, 데이터소스에서 얻거나 직접 만들 수 있다.

스파크에서 DataFrame의 각 로우는 하나의 레코드이다. 스파크는 레코드를 Row 객체로 표현한다. 스파크는 값을 생성하기 위해 컬럼 표현식으로 Row 객체를 다룬다. Row 객체는 내부에 바이트 배열을 가진다. 이 바이트 배열 인터페이스는 오직 컬럼 표현식으로만 다룰 수 있으므로 사용자에게 절대 노출되지 않는다.

DataFrame을 사용해 드라이버에게 개별 로우를 반환하는 명령은 항상 하나 이상의 Row 타입을 반환한다.

- Row 객체 생성하기

    ```python
    from pyspark.sql import Row
    
    my_row = Row('Hello', None, 1, False)
    ```

로우의 데이터에 접근하는 방법은 아주 쉽다. 원하는 위치를 지정하기만 하면 된다.

```python
my_row[0] # Hello
my_row[2] # 1
```

### 스파크 데이터 타입

------

```scala
from pyspark.sql.types import *

b = ByteType()
```

- 파이썬 데이터 타입 매핑

    | 스파크 데이터 타입                                           | 파이썬 데이터 타입                                           |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | ByteType                                                     | int, long.                                                   |
    | 숫자는 런타임에 1바이트 크기의 부호형 정수로 변환된다. (-128 ~ 127 사이의 값을 가짐) |                                                              |
    | ShortType                                                    | int, long.                                                   |
    | 숫자는 런타임에 2바이트 크기의 부호형 정스로 변환된다. (-32768 ~ 32767 사이의 값을 가짐) |                                                              |
    | IntegerType                                                  | int, long.                                                   |
    | 파이썬의 ‘정수형’ 데이터 타입의 숫자를 관대하게 정의한다. 매우 큰 숫자값을 IntegerType()에서 사용하면 스파크 SQL에서 거부할 수 있다.  (숫자값이 너무 크면 LongType을 사용해야 함) |                                                              |
    | LongType                                                     | long.                                                        |
    | 숫자는 런타임에 8바이트 크기의 부호형 정수로 변환된다. 더 큰 숫자를 사용하려면 값을 decimal.Decimal형 으로 변환해 DecimalType을 사용한다. |                                                              |
    | FloatType                                                    | float.                                                       |
    | 숫자는 런타임에 4바이트 크기의 single-precision 부동 소수점으로 변환된다. |                                                              |
    | DoubleType                                                   | float                                                        |
    | DecimalType                                                  | decimal.Decimal                                              |
    | StringType                                                   | string                                                       |
    | BinaryType                                                   | bytearray                                                    |
    | BooleanType                                                  | bool                                                         |
    | TimestampType                                                | datetime.datetime                                            |
    | DateType                                                     | datetime.date                                                |
    | ArrayType                                                    | list, tuple, array                                           |
    | MapType                                                      | dict                                                         |
    | StructType                                                   | list, tuple                                                  |
    | StructField                                                  | 이 필드의 데이터 타입과 대응되는 파이썬 데이터 타입이다. 예를 들어 IntegerType을 사용하는 StructField는 파이썬의 int 데이터 타입을 사용한다. |

DataFrame의 파티셔닝은 클러스터에서 물리적으로 배치되는 형태를 정의한다. 파티셔닝 스키마는 파티션을 배치하는 방법을 정의한다. 파티셔닝의 분할 기준은 특정 컬럼이나 비결정론적(매번 변하는) 값을 기반으로 설정할 수 있다.

### Transformation of DataFrame

------

DataFrame을 다루는 방법에 대해 알아본다.

- Create DataFrame

    ```python
    from pyspark.sql import Row
    from pyspark.sql.types import (
    		StructField,
    		StructType,
    		StringType,
    		LongType
    )
    
    my_manual_schema = StructType([
    		StructField('some', StringType(), True),
    		StructField('col', StringType(), True),
    		StructField('names', LongType(), False)
    ])
    
    my_raw = Row('Hello', None, 1)
    my_df = spark.createDataFrame([my_raw], my_manual_schema)
    ```