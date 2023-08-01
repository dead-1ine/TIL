### AWS Glue란?

---

-   완전 관리형 데이터 추출, 변환 및 적재 (ETL) 서비스
-   효율적인 비용으로 간단하게 여러 데이터 스토어 및 데이터 스트림 간에 원하는 데이터를 분류, 정리, 보강, 이동할 수 있다.



#### ETL이란?

---

-   Extract: 데이터 저장소로부터 데이터를 가져오는 것
-   Transform: 데이터를 조회 또는 분석의 목적으로 적절하게 포맷을 변경하는 것(ex. 3월 29일 -> 0329)
-   Load: 데이터 웨어하우스나 데이터 레이크, 데이터 저장 서비스로 저장하는 것



### AWS Glue 특징

---

-   서버리스이므로 설정하거나 관리할 인프라가 없다.
-   **원본 데이터의 변경 및 변경 데이터의 저장을 위한 별도의 저장소가 필요없고, 메타데이터만으로 ETL작업을 수행한다.**
-   **정형 데이터와 더불어 반정형 데이터도 함께 작동하도록 설계되었다.**
-   ETL 스크립트에서 사용할 수 있는 Dynamic Frame이라는 구성 요소를 사용하여 Apache Spark의 DataFrame과 완벽하게 호환되고, 스키마가 필요없으며, Dynamic Frame용 고급 변환세트로 이용할 수 있다.
-   고성능 워커로 빠른 작업 수행이 가능하다.
-   **스케줄링 기능으로 주기적인 작업 실행을 자동화할 수 있다.**
-   북마크 기능으로 작업상태를 저장하여 중단된 시점부터 작업 재개가 가능하다.
-   작업에 대한 모니터링을 지원한다.

---

![스크린샷 2021-09-15 오전 9.18.05](/Users/yang-wonseog/Library/Application Support/typora-user-images/스크린샷 2021-09-15 오전 9.18.05.png)

1.   **Data Store** : S3, RDS, Redshift, Kinesis, Apache Kafka 등의 데이터 저장 서비스나 데이터 스트림 서비스이다.
2.   **Classifier** : 데이터의 스키마를 결정하고 일반적인 파일들의 분류자를 제공한다.
3.   **Crawler** : Classifier의 우선 순위 지정 목록을 통해 데이터의 스키마를 결정한 다음, 메타 데이터 테이블을 생성한다.
4.   **Data Catalog** : 테이블 정의, 작업 정의 및 기타 관리 정보를 포함한다.
5.   **Job** : ETL 작업을 수행하는 데 필요한 변환 스크립트, 데이터 원본 및 데이터 대상으로 구성된 비즈니스 로직이다.
6.   **Connection** : AWS의 다른 데이터 저장 서비스나 사용자의 VPC환경 내부에 있는 데이터베이스에서 데이터 추출을 위한 장치이다.
7.   **Script** : Apache Spark에서 사용하는 PySpark, Scala 등으로 짜여진 ETL 작업 스크립트이다.
8.   **Schedule or Event** : Job이 실행되는 주기를 설정하거나, 혹은 특정 이벤트로 인한 트리거로 실행할 수 있다.



### Glue Studio

---

-   AWS Glue의 GUI로, ETL이 필요한 개발자들이 Glue에서 ETL 작업을 손쉽게 작성하여 실행 및 모니터링이 가능하다.
-   코드를 작성하지 않고 AWS Glue의 서버리스 Apache Spark 기반 ETL 플랫폼에서 빅데이터를 처리할 수 있다.

![스크린샷 2021-09-15 오전 10.04.24](/Users/yang-wonseog/Library/Application Support/typora-user-images/스크린샷 2021-09-15 오전 10.04.24.png)

-   Glue Studio를 통해 여러 데이터 소스에서 카탈로그로 메타데이터만 가져오고, ETL 작업 후 데이터를 저장하거나 엔드포인트를 생성하여 Sagemaker, EMR, QuickSight 등의 서비스로 연결할 수 있다.

![스크린샷 2021-09-15 오전 10.06.44](/Users/yang-wonseog/Library/Application Support/typora-user-images/스크린샷 2021-09-15 오전 10.06.44.png)



[출처 : https://aws.amazon.com/ko/glue]

