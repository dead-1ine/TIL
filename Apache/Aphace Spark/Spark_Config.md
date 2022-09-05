# Spark Config

spark의 config를 코드 단에서 설정하는 방법은 두 가지가 있다. 그 두 가지는 아래와 같다.

1. `sparksession.config()`
2. `spark.conf.set()`



## pyspark code, spark-submit, spark-defaults.conf의 적용 우선순위

Spark의 Config를 설정할 수 있는 방법은 크게 세 가지로 나뉜다. 아래는 config가 설정되는 우선순위를 순서에 맞게 나열한 것이다.

1. pyspark code

2. spark-submit

    spark-submit은 Spark의 bin 디렉터리에 있는 스크립트로, 클러스터에서 application을 수행하기 위해 사용된다.

    ```shell
    ./bin/spark-submit \
    --class <main-class> \
    --master <master-url> \
    --deploy-mode <deploy-mode> \
    --conf <key>=<value> \
    ... # other options
    <application-jar> \
    [application-arguments]
    ```

    

3. spark-defaults.conf

    spark-submit은 Spark의 디렉터리에서 conf/spark-defaults.conf를 찾은 후 파일에서 공백으로 구분된 키와 값의 쌍을 찾는다.



# Spark Property

스파크 프로퍼티는 스파크 애플리케이션 실행과 관련한 설정값을 의미한다.

설정값은 SparkConf 인스턴스를 통해 설정할 수 있다. 하지만 코드에 항상 포함되어야 하는 단점이 있다.

이를 해결하기 위한 방법은 아래와 같다.

- Spark Shell or spark-submit을 이용
- Spark Home의 spark-defaults.conf 파일에 각 프로퍼티를 정의

## 1) 어플리케이션 관련 설정

| Property Name                | Meaning                                                      | default             |
| ---------------------------- | ------------------------------------------------------------ | ------------------- |
| `spark.app.name`             | 어플리케이션 이름                                            | X(필수로 세팅 필요) |
| `spark.driver.cores`         | 드라이버가 사용할 코어의 수                                  | 1                   |
| `spark.driver.maxResultSize` | 액션 연산으로 생성된 값의 최대 크기                          | 1GB                 |
| `spark.driver.memory`        | 드라이버가 사용할 메모리의 크기                              | 1GB                 |
| `spark.executor.memory`      | 익스큐터 하나의 메모리 크기                                  | 1GB                 |
| `spark.local.dir`            | RDD 데이터 저장 혹은 셔플 시 Mapper의 데이터를 저장하는 경로 | /tmp                |
| `spark.master`               | 클러스터 매니저 정보                                         | -                   |
| `spark.submit.deployMode`    | Deploy Mode 설정(client or cluster)                          | -                   |

