### 개요

---

>   틈 날때마다 정리하는 Pandas 라이브러리 함수 및 팁 정리 파일



### 1. DataFrame

---

1.   행 추가하기

     ```python
     add_row = {(7, 'Column', 7, 'NewCastle')}
     df_add_row = pd.DataFrame(add_row, columns = ['순위', '이름', '득점 수', '소속팀'])
     df2 = df2.append(df_add_row)
     print(df2)
     ```

     

