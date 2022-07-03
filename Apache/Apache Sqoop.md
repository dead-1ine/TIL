# Apache Sqoop

​	Sqoop은 관계형 데이터베이스와 하둡 사이에서 데이터 이관을 지원하는 툴이다. 스쿱을 이용하면 관계형 데이터베이스의 데이터를 HDFS, Hive, Hbase에 import하거나 반대로 관계형 데이터베이스로 export할 수 있다.

​	Sqoop은 클라우데라에서 개발되었으며 현재 아파치 오픈소스 프로젝트로 공개되어 있다.



## 1. Sqoop Architecture

​	Sqoop은 관계형 데이터베이스를 읽고 쓸 수 있는 Connector라는 개념을 사용한다. Connector는 각 데이터베이스별로 구현되어 있으며, JDBC 드라이버를 이용해 데이터베이스 접속 및 쿼리 실행을 요청한다.



### 1) Import Data 동작 방식

1. 클라이언트가 Sqoop에 import를 요청.
    클라이언트는 데이터베이스 접속 정보, import 대상 테이블, import 쿼리, 실행할 맵 태스크 갯수 등을 설정
2. Sqoop은 데이터베이스에서 해당 테이블의 메타데이터를 조회하여 ORM(Object Relational Mapping) 클래스를 생성.
    ORM 클래스에는 export 대상 테이블의 컬럼을 자바 변수로 매핑하고, 맵리듀스 잡 실행에 필요한 직렬화 메소드를 생성.
3. Sqoop은 ORM 클래스가 정상적으로 생성되면 맵리듀스 잡 실행을 요청.
    Sqoop은 Map 태스크의 출력 결과를 import에 사용하여 Reduce 태스크는 실행되지 않음.
4. Map 태스크는 데이터베이스에 JDBC로 접속한 후 SELECT 쿼리를 실행.
    이 때 쿼리문은 사용자가 직접 설정한 쿼리일 수도 있고, 사용자가 테이블만 설정했을 경우에는 ORM 클래스를 이용해 쿼리를 설정.
    Sqoop은 대상 테이블의 Primary Key의 최소값과 최대값을 조회 후 데이터가 균등하게 분포되도록 쿼리문을 수정.
5. Map 태스크는 쿼리문을 실행한 결과를 HDFS에 저장.
    전체 Map 태스크가 종료되면 Sqoop은 클라이언트에게 작업이 종료되었다고 알림.
6. 사용자가 설정한 Hive 테이블 생성.
7. Map 태스크에 저장된 결과를 Hive 테이블의 데이터 경로로 로딩.



### 2) Export Data 동작 방식

1. 클라이언트는 Sqoop에 export를 요청.
2. Sqoop은 데이터베이스에서 메타데이터를 조회 후 맵리듀스 잡에서 사용할 ORM 클래스를 생성.
3. Sqoop은 데이터베이스의 중간 테이블의 데이터를 모두 삭제한 후 맵리듀스 잡을 실행.
4. Map 태스크는 HDFS에서 데이터를 조회한 후 INSERT 쿼리문을 만들어 중간 테이블에 데이터를 입력.
    이 때 쿼리문은 레코드당 한 번씩 실행하는 것이 아닌 천 개 단위로 배치 실행.
    중간 테이블 사용여부와 배치 단위는 `sqoop.export.records.per.statement` 옵션으로 수정 가능.
5. Sqoop은 맵리듀스 잡이 정상적으로 종료되면 중간 테이블의 결과를 최종 테이블에 입력.
    (예를 들어, 중간 테이블명이 `tmp_table_1`, 최종 테이블이 `table_1`이라면(INESRT INTO table_1 (SELECT * from temp_table_1))의 쿼리를 실행한다.)