Redshift는 AWS의 MPP(Massive Parallel Processing) DB이다.

### Redshift의 큰 특징 두가지

1. Massive Parallel Processing
    다수의 컴퓨팅 노드가 각 노드의 코어마다 전체 데이터를 분할하여 동일하게 컴파일된 쿼리 세그먼트를 실행한다. 
    데이터를 병렬로 처리할 수 있도록 테이블의 행을 계산하여 노드에 배포한다.
    각 테이블마다 적절한 분산 키를 선택하면 데이터 분산을 최적화할 수 있다.
2. Columnar Data Storage
    데이터베이스 테이블 정보를 열 기반 방식으로 저장하기 때문에 디스크 I/O 요청 수나 디스크에서 로드하는 데이터 크기를 감소시킬 수 있다.



