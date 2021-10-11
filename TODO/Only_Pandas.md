### 개요

---

>   틈 날때마다 정리하는 Pandas 라이브러리 함수 및 팁 정리 파일



### Pandas란?

---

-   테이블형 데이터를 다룰 수 있는 다양한 기능을 지닌 라이브러리
    -   파이썬에서 데이터분석을 위해 기본적으로 사용하는 라이브러리임
-   raw data를 데이터 분석 전과정을 위해 사용할 수 있도록 변환하는 데이터 전처리에도 많이 사용됨
    -   raw data: 데이터 분석 전 정제되지 않은 기본 데이터를 의미
        -   보통 데이터 분석 목적에 맞지 않는 불필요한 데이터나 데이터가 없는 열들을 의미함

### 1. DataFrame

---

1.   행 추가하기

     ```python
     add_row = {(7, 'Column', 7, 'NewCastle')}
     df_add_row = pd.DataFrame(add_row, columns = ['순위', '이름', '득점 수', '소속팀'])
     df2 = df2.append(df_add_row)
     print(df2)
     ```

     

