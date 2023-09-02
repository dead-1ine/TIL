# 1주차(8월 28일 ~ 9월 1일)

## 1. 알아보고 정리할 것들

------

- [ ]  입출력 스트림

- [ ]  Spark로 parquet를 읽었을 때, `Found Duplicate column(s) in the data schema` 를 어떻게 해결할 수 있을까?

    - Error info

        ```
        An error was encountered:
        Found duplicate column(s) in the data schema: `user_properties.[appsflyer]_apple_keyword_id`
        Traceback (most recent call last):
          File "/mnt1/yarn/usercache/livy/appcache/application_1693441232880_0001/container_1693441232880_0001_01_000001/pyspark.zip/pyspark/sql/readwriter.py", line 182, in load
            return self._df(self._jreader.load(self._spark._sc._jvm.PythonUtils.toSeq(path)))
          File "/mnt1/yarn/usercache/livy/appcache/application_1693441232880_0001/container_1693441232880_0001_01_000001/py4j-0.10.9.5-src.zip/py4j/java_gateway.py", line 1322, in __call__
            answer, self.gateway_client, self.target_id, self.name)
          File "/mnt1/yarn/usercache/livy/appcache/application_1693441232880_0001/container_1693441232880_0001_01_000001/pyspark.zip/pyspark/sql/utils.py", line 196, in deco
            raise converted from None
        pyspark.sql.utils.AnalysisException: Found duplicate column(s) in the data schema: `user_properties.[appsflyer]_apple_keyword_id``
        ```

- [ ]  Python tutor를 통해 Class들이 실제로 메모리를 어떻게 사용하고, 기능을 어떻게 적용시키는지에 대한 개념 파악하기

- [ ]  Python에서 실제 메모리를 어떻게 사용하는지 알려주는 CLI 등을 찾아보기

## 2. Information

------

### 2-1. 기타 등등

- 무언가를 동적으로 할당한다는 것은 Runtime 시 할당된다는 것을 의미한다.

### 2-2. Python - 객체지향 - class.**init**()

- `class` 에 따로 `__init__()` 이 구현되어 있지 않다면, 해당 `class` 가 상속받은 상위 클래스의 `__init__()` 을 사용한다.

### 2-3. Python - 객체지향 - Mixin Class

- `Mixin` 클래스는 특정 기능을 구현해놓은 재사용 가능한 코드이다. `Mixin` 클래스는 독립적으로 사용되기보다는 다른 클래스에 기능을 **“Mix In”** 하기 위해 존재하며 상속을 통해 사용된다.
- 일반적으로 `Mixin` 클래스는 하나의 명확한 기능을 제공하도록 설계되어 있으며, 이를 통해 코드의 재사용성을 높이고 유지보수성을 개선할 수 있다.

### 2-4. Spark - No such file or directory

Spark는 Lazy Evaluation을 한다. `read.format(parquet).load(path)` 를 수행하여 이를 변수에 할당하면, 해당 변수는 `load(path)` 에 해당하는 주소의 실제 파일들을 리스트로 가지고 있는다.

첫 action에는 제대로 동작하였으나, `load(path)` 에 사용된 path의 파일들을 다시 적재할 상황이 생겨 새로 적재하고 두 번째 action을 수행하니 `No such file or directory` 라는 에러가 발생하였다.

- 상세한 에러 내용

    ```
    An error was encountered:
    An error occurred while calling o171.collectToPython.
    : org.apache.spark.SparkException: Job aborted due to stage failure: Task 2 in stage 17.0 failed 4 times, most recent failure: Lost task 2.3 in stage 17.0 (TID 1018) (ip-10-64-0-36.ap-northeast-2.compute.internal executor 58): java.io.FileNotFoundException: 
    No such file or directory 's3://brandi-data-datalake-prod-impressions/brandi/roas/daily-v4/2022/06/01/part-00350-da89dd73-b362-492a-b835-53b811cf03ae-c000.snappy.parquet'
    ```

## 3. Thinking

------

### 3-1. 매 주 필요한 일들을 꾸준히 해보자.

- 하루 정도는 강의를 듣고 싶다.
- 매 주마다 나눠서 해야할 일들을 정리하면 다음과 같다.
    - 강의 듣기
    - 영어 공부
    - 사이드 프로젝트
    - 생각정리
    - 신기술 찾기 및 로컬에서 테스트해보기
    - 코딩 테스트
- 학습에 대한 로드맵을 정할 때는 강의 사이트의 커리큘럼을 참고하면 도움이 될 것이다.
- 백엔드 엔지니어에게 Airflow를 설명하려면, 그 분들에게 익숙한 라이브러리인 ArgoCD, Jenkins 등으로 예시를 두는 것이 좋겠다. (물론 내가 두 배 노력해야 하지만)
- 내 이력서에서 프로젝트에 대한 글들에 요약을 달아두자. 그래야 긴 글을 더 읽지 않고도 해당 프로젝트에 대한 요약을 통해 쉽게 알 수 있고 이를 통해 나를 더 어필하기 쉬워진다.

### 3-2. 내가 속한 도메인의 공통사항을 우선순위에 둔다. (feat. 순철님)

- 현재 내 포지션이 여러 도메인에서 공통적으로 수행하는 작업들 (예를 들어 데이터 레이크 구축, 데이터 분산 처리 프레임워크 잘 사용, 데이터 도메인 지식)을 먼저 잘 처리하는 것이 중요하다고 생각된다.
- 만약 여러 도메인에서 공통적으로 요구하는 작업에 대해 익숙하다면 그 다음이 나만의 색을 입히는 것이라 생각된다.
- 순철님의 경우는 도메인을 커머스로 둔 상태에서 말씀하셨다. 커머스에서의 ML 도입 공통 사항으론 쿠폰 최적화, 상품 추천, CRM이며 이에 따라 프로젝트에 우선순위를 두었다고 하셨다. 이 것들을 완료한 이후 안정화한 다음 각 플랫폼만의 성격을 입혀 특화된 모델을 만들어야 한다고 하셨다. (성격을 입히는 것은 내가 얘기하긴 했지만 순철님도 동의하셨다.)

### 3-3. 작업 시 생각난 것들

- 종종 for문을 사용하여 작업에 대한 반복을 수행한다. 이 때 항상 주의할 점은 변수이며, 항상 사용할 때 변수의 내용을 확인해본 이후 실제 로직을 적용시켜 실제 작업을 수행하도록 하자. (이번에는 날짜를 잘못 넣어 같은 변수의 날짜를 가지고 12달에 해당하는 parquet를 저장시켜버리는 실수를 저질렀다.)
- 로컬에서 Spark와 Airflow 등을 설치하고 이 기술들이 실제로 하드웨어를 어떻게 이용하고 있는지 직접 눈으로 확인해보자.
- 회사에서 사용하는 익숙한 기법들이 실제로 알맞게 사용하고 있는 것인지 확인해볼 필요성이 있다.

### 3-4. 나에 대한 질문들 - 나는 무엇을 모르는가?

1. 나는 Spark Application의 특정 로직이 어느 정도의 하드웨어 성능을 가져야 최적화된 것인지 알지 못한다.
2. 나는 Airflow DB의 구조를 모른다. (매우 간단하게만 알지 실제로 뜯어보지 않았다)
3. 나는 Airflow의 실제 동작 과정에 대한 간략한 정보만 알 뿐이지 매우 상세히 각 요소들의 작동을 설명하라고 하면 일부 못하는 부분들이 많다.

### 3-5. 한 권으로 읽는 컴퓨터 구조와 프로그래밍에서 개발자 노하우 관련 챕터를 읽고.

- 해법을 찾기 어렵다면 한 걸음 뒤로 물러서서 문제를 다시 재구성해보는 것이 중요하다. 하지만 열정적인 논의가 벌어지는 도중에 이런 사실을 기억하기는 어렵다.

    → **열정적인 논의 중에도 이렇게 한 걸음 뒤로 물러서서 생각할 수 있는 메타인지를 기르자!**

- 무엇보다도 기본이 탄탄해야 한다. 그래야 신기술에 대해서 빠르게 습득할 수 있다.

    → 컴퓨터 공학적 지식을 잘 갖추어야 한다. 그래야만이 갈 수록 차별화된 엔지니어가 될 수 있다.

- 해보지도 않은 일을 할 수 있는지 어떻게 알 수 있을까? 추정을 통해 배울 수 있다. 추정은 단순한 추측이 아니고, 경험을 바탕으로 하는 직관적 어림짐작이다.

- 셸이 제공하는 기능 중에는 명령을 파일에 넣어서 실행될 수 있는 프로그램을 만드는 강력한 기능이 있다. 여러분이 어떤 일을 수행하기 위해 같은 명령들을 계속 반복해 사용한다면, 이 일을 하는 명령을 파일에 넣어서 새로운 명령을 직접 만들 수 있다. 이런 식으로 명령을 만들어 활용하면 보기 좋은 그래픽 화면에서 버튼을 클릭하고 결과를 기다리는 것보다 훨씬 더 생산적으로 일할 수 있다.

## 글감

------

## 1. `.zshrc` 에 없는 명령어들은 어떻게 실행이 가능한 것인가?

- 만약 Conda를 사용하면 Terminal에 진입했을 때 `(env_name) $` 으로 뜰 것이다. 이 때는 `/Users/{user_name}/opt/anaconda3/bin/{cmd_name}` 에 포함되어 있는 것들은 바로 사용할 수 있도록 되어있기 때문이다.
- 기본적으로 모든 명령어는 bin 폴더 내부에 속해있으며, 이는 `.zshrc` 등과 같은 시작 명령어를 통해 환경변수에 등록되어 있기 때문이다.

## Eng

------

- locale: 현장
- equivalent: 동등한
- correspond: 일치하다
- verbosity: 수다, 다변
- intercept: 가로막다[가로채다]
- diagnose: 진단하다