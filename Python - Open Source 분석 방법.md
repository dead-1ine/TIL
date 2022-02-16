- 출처 : https://zzsza.github.io/development/2020/07/19/opensource-analysis/
- "어쩐지 오늘은" 이라는 블로그에서 읽은 글을 정리하였습니다.

- 이 글은 "어쩐지 오늘은"의 작성자가 개인적으로 시도한 방법을 정리한 것이다.

### 목차
1. Open Source란?
2. Open Source를 분석하면 좋은 점
3. 기본 지식
4. Open Source 선택하기
5. 공식 문서를 토대로 Open Source 파악하기
6. Clone 또는 Fork
7. 큰 숲 바라보기 - 아키텍처 분석
8. 디테일 분석 - 함수, 클래스 등
9. 팁
10. 같이 분석해보기 - SimPy
11. 마치며


### Open Source란?
---
- Wiki에 의하면 오픈소스 소프트웨어는 소스 코드를 공개해 누구나 제한없이 사용할 수 있는 오픈소스 라이선스를 만족하는 소프트웨어를 뜻함
	- 라이선스 종류 : Apache License, GNU, MIT, BSD 등
- 데이터 분석을 한다면 자주 사용할 Pandas, Numpy, Scikit Learn, TensorFlow, PyTorch, MXNet 등이 이에 해당한다.


### Open Source를 분석하면 좋은 점
---
> 필자의 개인적으로 생각하는 좋은 점임

	1. 본인이 익숙한 라이브러리의 내부를 알 수 있다.
	2. 코드 퀄리티를 향상할 수 있다.
		1. 파이썬 프로그래밍 방식
		2. Low Level에선 코드를 어떻게 추상화하는지 파악할 수 있음
	3. 오픈소스 기여를 위한 사전 단계
	4. 다양한 지식을 추가로 습득할 수 있다.
	5. 오픈소스의 버그를 찾을 수 있다.
	6. 메타인지를 가질 수 있다.

