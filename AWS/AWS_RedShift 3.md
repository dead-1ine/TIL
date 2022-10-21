Redshift는 AWS의 MPP(Massive Parallel Processing) DB이다.

### Redshift의 큰 특징 두가지

1. Massive Parallel Processing
    다수의 컴퓨팅 노드가 각 노드의 코어마다 전체 데이터를 분할하여 동일하게 컴파일된 쿼리 세그먼트를 실행한다. 
    데이터를 병렬로 처리할 수 있도록 테이블의 행을 계산하여 노드에 배포한다.
    각 테이블마다 적절한 분산 키를 선택하면 데이터 분산을 최적화할 수 있다.
2. Columnar Data Storage
    데이터베이스 테이블 정보를 열 기반 방식으로 저장하기 때문에 디스크 I/O 요청 수나 디스크에서 로드하는 데이터 크기를 감소시킬 수 있다.



### Redshift의 특징들

#### Cluster

Redshift는 클러스터로 구성되어 있으며, 리더 노드와 하나 이상의 컴퓨팅 노드로 구성되어 있다. 외부 애플리케이션은 리더 노드와 통신한다.

### OLTP 기능

데이터 삽입 및 삭제와 같은 온라인 트랜잭션(OLTP) 기능을 포함하여 일반적인 RDBMS와 동일한 기능을 제공하지만 이 중 특히 매우 큰 데이터 세트의 분석에 최적화되어 있다.

#### 데이터 압축

디스크 I/O를 떨어뜨림으로써 쿼리 성능이 향상되는 효과가 있다. 쿼리를 실행하면 압축된 데이터를 메모리로 읽어온 후 쿼리 실행 도중 압축이 해제된다.



## Redshift가 PostgreSQL과 다른 점

### 보조 인덱스가 없다.

보조 인덱스 작업과 같이 소규모 OLTP 처리 작업에 적합한 PostgreSQL 기능은 성능 개선을 위해 제외되었다.

### 지원하지 않는 쿼리 형식

- ALTER COLUMN 타입의 명령 불가
- ADD COLUMN은 각 ALTER TABLE 명령 당 한 개의 컬럼만 가능
- INSERT, UPDATE, DELETE 사용 시 With clause를 지원하지 않음

### COPY

COPY 명령은 테이블을 로드하는 가장 효율적인 방법이다. INSERT 명령을 사용하여 데이터를 테이블에 추가할 수도 있지만 COPY를 사용하는 것보다 효율은 떨어진다.

```sql
COPY table_name [ columns ]
FROM data_source authorization [ [ FORAMT ] [ AS ] data_format ] [ parameter [ argument ] [, ...] ]
```

### Vacuum

PostgreSQL은 기본적으로 VACUUM 작업이 공간을 재사용할 수 있도록 회수하는 데 그치는 반면, Redshift는 VACUUM FULL이 기본 VACUUM 작업으로써 디스크 공간을 회수한 후 모든 행을 재정렬한다.