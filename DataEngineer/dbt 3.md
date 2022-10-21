# dbt

Transform을 위한 도구, 기존의 ETL에서 ELT로의 변화 이후 개선을 위해 dbt와 같은 Tranform을 담당하는 도구가 대두되었다. 외부 데이터 소스로부터 데이터를 추출하거나 적재하는 기능은 없다. 이미 적재되어 있는 데ㅣ터를 조회하고 수정하는 데에 최적화된 도구이다.

dbt가 제안하는 방법은 다음과 같다. External Source -> Extract & Loader -> Data Warehouse -> Consumer 이다. 이 부분 중 Warehouse에서 일어나는 모든 Transform을 모두 dbt가 담당하는 것이다.

dbt는 이러한 데이터의 가공 과정을 Modeling이라는 용어로 표현한다.
