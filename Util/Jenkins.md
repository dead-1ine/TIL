# Jenkins

젠킨스는 소프트웨어 개발 시 지속적으로 통합 서비스를 제공하는 툴이다. CI(Continuous Integration) 툴이라고 표현한다.

다수의 개발자들이 하나의 프로그램을 개발할 때 버전 충돌을 방지하기 위해 각자 작업한 내용을 공유 영역에 있는 저장소에 빈번히 업로드함으로써 지속적 통합이 가능하도록 해준다.

젠킨스와 같은 CI툴이 등장하기 전에는 일정시간마다 빌드를 실행하는 방식이 일반적이었다. 특히 개발자들이 당일 작성한 소스들의 커밋이 모두 끝난 심야 시간대에 이러한 빌드가 스케줄러에 의해 집중적으로 진행되었는데 이를 nightly-build라고 한다.

하지만 젠킨스는 정기적인 빌드에서 한 발 나아가 서브버전, Git과 같은 버전관리 시스템과 연동하여 소스의 커밋을 감지하면 자동화 테스트가 포함된 빌드가 작동되도록 설정할 수 있다.



## 젠킨스가 주는 이점

개발중인 프로젝트에서 커밋은 매우 빈번히 일어나기 때문에 커밋의 횟수만큼 빌드를 실행하는 것이 아니라 작업이 큐잉되어 자신이 실행할 차례를 기다리게 된다.

코드의 변경과 함께 이뤄지는 이 같은 자동화된 빌드와 테스트 작업들은 다음과 같은 이점들을 가져다 준다.

- 프로젝트 표준 컴파일 환경에서의 컴파일 오류 검출
- 자동화 테스트 수행
- 정적 코드 분석에 의한 코딩 규약 준수여부 체크
- 프로파일링 툴을 이용한 