# 2023-07-2(10~14)

- [ ]  검색 도메인에 대한 기본 지식: 색인, 역색인

- [ ]  모르는 것 알아보기:

    - [ ]  GRPC

    - [ ]  

        파티셔닝과 버켓팅

        - [ ]  SQL: Rollup, Cube

    - [ ]  Apache Ranger

    - [ ] 암시적 형변환



## Spark UI를 보며 partition 최적화

---

> Spark UI를 보며 최적화를 잘 하려면 Spark의 내부 구조와 원리 및 처리 과정에 대해 깊이 이해해야 한다. (내가 부족해서 하는 소리다)

- 깨달은 점

    - S3(등의 저장소)에서 Parquet(등의 file)을 읽은 후 persist()를 하지 않으면 계속 읽으러 간다. (적어도 UI의 DAG Visualization에는 그렇게 나온다. 다음에 해당 작업의 상태가 Skipped되어 있는지 확인하자. Spark는 인메모리 기반이므로 데이터를 메모리에 올려두고 처리한다. 이 때 처리할 대상이 되는 데이터가 메모리에 올라가 있으면 처리 작업에서 Skipped된다.)

    - `persist()`를 제대로 사용하는 방법

        Spark의 `persist()`는 기존의 DataFrame을 변경하지 않고 새로운 DataFrame을 반환한다. 이 새로운 DataFrame은 원래 DataFrame을 메모리에 캐싱하는 특성을 가진다.

        `persist()`는 DataFrame을 메모리에 캐싱하여 여러 번 사용할 때 계산을 재사용하고, 불필요한 I/O를 방지하여 성능을 향상시키는 데 사용된ㄷ다. 이는 특히 같은 DataFrame을 여러 번 Action해야할 때 사용 시 매우 유용하다.

        따라서, `persist()`를 호출하면 반환된 DataFrame을 새로운 변수에 할당 후 사용해야 하며, 그렇지 않으면 캐싱된 DataFrame에 대한 참조를 잃으므로 `persist()`의 효과를 받지 못한다.

        아래의 예시는 잘못된 사용법과 옳은 사용법을 코드로 표현하였다.

        ```python
        ## 잘못된 사용법
        exist_df  # 기존 DataFrame
        exist_df.persist()  # 캐싱하였으나 새로운 DataFrame을 참조하지 않아 캐싱의 효과를 받지 못함
        
        exist_df.show()  # 캐싱되지 않은 원래의 DataFrame을 참조함
        
        ## 옳은 사용법
        exist_df  # 기존 DataFrame
        cached_df = exist_df.persist()
        
        cached_df.show()  # 제대로 캐싱된 DataFrame을 참조함
        ```

    - `persist()`를 제대로 사용하는 방법에 이어서 반대 메서드인 `unpersist()`에 대한 설명

        `unpersist()`는 DataFrame이나 캐싱된 데이터를 메모리에서 제거한다. 이 메서드는 해당 DataFrame 자체를 메모리에서 제거하는 것이 아닌, `persist()` 혹은 `cache() <- (persist()의 하위 호환에 해당하는 메서드)`에 의해 캐싱된 데이터만을 메모리에서 제거한다.

        `unpersist()`는 캐싱된 데이터를 메모리에서 제거하고 원래의 DataFrame을 반환한다. 하지만 이 반환값은 일반적으로 사용하지 않는다.

        `unpersist()`의 주요 목적은 캐싱된 DataFrame을 제거하여 메모리를 해제하는 것이기 때문이다. 따라서 **`unpersist()`는 메모리의 사용량을 줄이고자 할 때 주로 사용된다.**

    - `df.repartition(n).persist()`처럼 `repartition()``과 `persist()``가 함께 쓰일 때의 내부 동작

        `persist()`를 호출하면 해당 시점에서의 DataFrame의 상태를 메모리에 캐싱하게 된다. 만약 `df.repartition(50).persist()`와 같이 `repartition()` 이후에 `persist()`를 사용하면 repartitoin된 결과가 메모리에 캐싱되어 재사용할 수 있게 된다.

        하지만, `persist()`와 `repartition()` 모두 메모리를 사용하므로 사용 가능한 메모리 리소스를 고려하여 적절히 사용해야 한다. 

        또한 Spark의 Lazy Evaluation 특성으로 인해 `persist()`는 호출 이후 실제로 데이터가 메모리에 캐싱되는 시점은 Action이 호출될 때이다. (예: `count()`, `show()`, `collect()`)

    - Spark Cluster의 병렬성과 관련한 옵션들

        Spark Cluster는 병렬성을 제어하는 몇 가지의 유용한 설정을 가지고 있다.

        1. `spark.executor.cores`: 각 Executor가 사용하는 코어 수를 설정한다. 이 수가 늘어나면 각 Executor는 더 많은 Task를 동시에 처리할 수 있다. 하지만 이 수가 늘어나면 각 Task가 사용할 수 있는 CPU 리소스가 줄어든다.(당연하게도) 이 설정은 사용할 수 있는 코어의 총 갯수에 따라 달라진다.(이 설정을 했을 경우 내부적으로 어떻게 사용하는지 알아보고 싶다)
        2. `spark.default.parallelism`: Spark Job의 기본 병렬성 수준을 설정한다. 이 값은 Spark Cluster의 전체 작업량을 결정하는 데 사용된다.
        3. `spark.sql.shuffle.partitions`: Spark SQL에서 셔플 연산 이후 생성되는 파티션의 수를 제어한다. 이 값이 너무 작으면 셔플 이후 너무 많은 파티션이 생성될 수 있고, 너무 크면 큰 파티션이 생성될 수 있다. 따라서 어느 한 쪽으로 치우치지 않게 적절한 수를 설정하는 것이 좋다.
        4. `spark.dynamic.Allocation.enabled`: (더 알아보자)

    - Spark Cluster에서 사용하는 Worker Node의 Instance 최적화(**처리하는 데이터를 생각하고, 이 데이터에 최적화된 Instance를 설정할 수 있는 것이 엔지니어의 역할이다.**)

    

    

## Information

- SQL

    - `LIMIT`: 

        데이터개발팀장님께 bi-mart라 불리는 데이터베이스의 특정 테이블들에 대한 접근 권한을 팀 계정에 부여해달라는 요청을 했다. 이 때 권한들이 제대로 부여되었는지 확인하기 위해 평소와 같이 `SELECT * FROM [TABLE_NAME]`으로 조회가 가능한지 확인해보았다. 하지만 시간이 너무 오래 걸렸고, 특정 조건 없이 특정 테이블에 대한 전체 조회를 진행하면 DB에 부하가 걸린다는 것을 알았다. 이 때 사용하면 좋은 것이 바로 이 `LIMIT`이다. (예: `SELECT * FROM [TABLE_NAME] LIMIT 1 --1개의 레코드를 반환한다.`)

        `LIMIT`을 사용하면 반환되는 레코드의 수를 제한하여 서버에 부하를 해결하고 데이터의 반환시간을 크게 단축시킨다. 하지만 항상 DB의 부하를 줄이는 것은 아니다. `LIMIT`이 포함된 쿼리가 DB에서 효율적으로 실행되려면 적절한 인덱스가 있어야 한다. 그렇지 않으면, DB에서 발생하는 부하를 크게 줄이지 못할 수 있다.
        
        

## Thinking

------

- 이력서를 정리할 때 내게 필요한 것:
    - Data Engineer의 JD를 보자
        - JD를 보면 내가 어떤 것이 부족하고, 어떤 것을 강점으로 내비칠 수 있는지 생각할 수 있게 된다.
        - 강점은 포트폴리오로 정리하고, 약점은 글을 쓰며 강점으로 바꿔보자. (요즘은 Open Source를 분석하는 것에 흥미를 느끼고 있고, 이를 글로 써서 내가 이 정도로 이 직업과 프로그래밍에 흥미를 가지고 있는 사람이라는 것을 공유하자)
    - 글을 쓰자:
        - 업무 시에 고민했던 것들을 구체화하여 블로그에 정리해두자.
            - (이번 주 금요일에는 Spark로 데이터를 backfilling할 일이 있었다. 이 때 이상하게 너무 오래걸리는 부분이 존재하여 Spark UI를 보며 오래 걸리는 부분을 발견하고 이를 수정하여 문제를 해결하였다. (물론 여전히 오래 걸리기에 아직 더 손을 봐야 한다))
        - 취미 삼아 행했던 Open Source 분석 등의 작업을 글로 발행하여 나를 알리자.
- Spark UI를 보며 Spark Job을 최적화하려면, Spark의 내부 구조와 처리 과정에 대한 이해가 필요하다. 나는 이 부분이 부족하여 문제에 봉착했을 때, 허둥지둥 너무 오래 걸리는 편이다. **이를 해결하려면, 내가 현재 사용하고 있는 코드의 특정 메서드에서 부터 실제 Spark Cluster에서 동작하는 과정에 대해 알아보는 과정이 필요하다.**
- 데이터를 backfilling하는 과정에서 든 생각:
    - 어떻게 하면 비용을 줄이면서 같은 양의 데이터를 처리하여 최종적으로 저장할 수 있을까?
    - 현재 backfilling의 대상이 되는 저장소는 AWS S3이다. S3의 비용 정책은 요청 당 비용이 발생하는 구조를 가지는데, Standard 기준 PUT, COPY, POST, LIST(요청 1,000개 당) 0.0045USD(약 5.17원), GET, SELET 및 기타 모든 요청(요청 1,000개 당) 0.00035USD(약 0.44원)이 발생한다.
    - 비용을 줄이는 방법 중 하나로, 적재하는 데이터의 파일의 총 갯수를 줄이는 것이다. 이는 단순 S3 비용을 줄이는 것을 넘어 앞으로 사용하게 될 Query Engine(Spark 등)의 리소스 비용 또한 크게 줄인다. 만약 parquet 파일을 저장한다고 가정했을 때, 한 개당 128MB ~ 1GB가 적당하다.
- 자동화를 좋아하는 사람으로써, 머신러닝 기법을 아는 것은 또 다른 다양한 범위에 대한 자동화가 가능하게 된다. 엔지니어링에 대해 이해한 후 머신러닝 쪽으로 넘어가자.

### Information

------

- Intellij 단축키:

    - F2: 가장 가까운 에러나 경고로 커서 이동

- Airflow:

    - trigger_rule은 바로 앞 Task(direct upstream)의 상태에만 해당되는 것이다. 해당 Task보다 더 상위 단계의 upstream Task의 상태는 고려하지 않는다는 것이다. 이는 Airflow의 DAG가 해당 DAG에 속한 전체 Task의 흐름에 의존성을 가지는 것이 아니라, 각각의 Task를 직접적으로 연결하는 의존성만으로 작동한다는 의미이다.

- Vim:

    - ```
        /
        ```

         \+ 

        ```
        Ctrl-R
        ```

         \+ 

        ```
        "
        ```

         : 현재 클립보드에 있는 단어를 바로 검색

        - `Ctrl-R` : register를 입력
        - `“` : 클립보드의 내용을 입력

    - `Ctrl-o` : 이전 커서 위치로 돌아가기

    - `Ctrl-i` : 앞 커서 위치로 돌아가기

    - ```
        yiw
        ```

         : 현재 커서 위치가 포함되어 있는 단어를 복사

        - `y` : yank의 약
        - `i` : inside의 약자
        - `w` : word의 약자

- Open Source 분석하기

    - 코드 흐름 추적하기: 간단한 기능이나 클래스를 찾아, 그것이 어떻게 동작하는지, 어디에서 호출되는지 파악하려고 노력하세요. 이런 식으로 전체 코드 흐름을 이해할 수 있습니다.
    - 정기적으로 코드 리뷰하기: 일정 시간 동안 코딩을 계속하면서 무엇을 배웠는지, 어떤 부분이 개선되었는지 리뷰하는 습관을 가지세요. 이를 통해 학습 과정을 반복하고 지속적으로 성장할 수 있습니다.
    - 프로젝트 이해: 프로젝트의 README, 문서, 위키 등을 읽어보세요. 프로젝트의 전체 구조와 개별부분이 어떻게 동작하는지 이해하는 것이 중요합니다.
    - 작은 부분부터 시작하기: 전체 코드베이스를 한 번에 이해하려고 하지 마세요. 대신, 작은 부분 또는 특정 기능부터 시작하세요. 그런 다음, 코드가 어떻게 동작하는지, 왜 그런 방식으로 작성되었는지 이해하려고 노력하세요.

- Data Platform을 DataLake 기반으로 사용하면 생기는 이점

    - RDB에 접근하기 어려운 비개발자들에 더 나은 접근성  제공
        - SQL이 능숙하지 않은 구성원에게 SQL이라는 것도 큰 장벽인데, 각 도메인 테이블의 맥락까지 스스로 찾아보거나 분석팀을 찾아가 물어봐야 한다면, 시간도 많이 걸리고 Lean하게 확인할 수 있는 업무가 불필요하게 커져 버릴 수 있습니다.
        - Data Discovery Platform은 분석 환경에 있는 모든 데이터를 쉽게 검색하고, 빠르고 쉽게 이해할 수 있는 플랫폼입니다. 분석 환경에 어떤 테이블이 있는지와 함께, 그 테이블의 Meta Data도 볼 수 있을 뿐 아니라, 테이블을 생성하는 책임자, 관련된 문서들과 대시보드의 어떤 지표에서 활용되고 있는지, 어떤 Product의 Feature에 적용되어 있는지까지 관리할 수 있는 데이터 중앙 플랫폼입니다.
        - 출처: ([뱅크샐러드 Data Discovery Platform의 시작](https://www.notion.so/July-22978def0cec4cedb22ef455c57aca79?pvs=21))

- Toss의 데이터 이관 작업 중 정합성을 확인하는 과정은 아래와 같다.

    ```jsx
    new_df = new_df.drop_duplicates()
    
    origin_df_count = origin_df.count()
    new_df_count = new_df.count()
    
    total_df = new_df.unionByName(origin_df, allowMissingColumns=True)
    total_df = total_df.drop_duplicates()
    total_df_count = total_df.count()
    
    if total_df_count != new_df_count:
    		print("Different Data!!")
    ```

### English

------

- indispensable: 필수적인, 없어서는 안될
- derive: 기원에 두다