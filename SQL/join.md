> 두 개 이상의 테이블을 결합하여 나타낼 때 사용한다.

## INNER JOIN
---
![[9BC70D4B-9DE7-4F44-9E1D-CE888693CB36.png]]
> Inner Join은 위와 같이 우리가 조인하고자 하는 두 개의 테이블에서 공통된 요소들을 통해 결합하는 조인방식이다.

- 예시
```sql
SELECT table1.col1, table1.col2, ..., table2.col1, table2.col2
FROM table1 [table1의 별칭]
JOIN table2 [table2의 별칭] ON table1.col1 = table2.col2
```

- 조인 시에 table1과 table2에서 어떤  컬럼을 기준으로 조인할지 ON 뒤에 작성한다.

<<<<<<< HEAD
=======
= 교집합

>>>>>>> 1b160f68c7b620f1fcb6ecfa1ab2f1a8c49dc467
## OUTER JOIN
---
![[CA57C7DA-954C-4035-A1D1-44823695E756.png]]
> Outer Join은 그림과 같이 Left Outer Join, Right Outer Join 그리고 그 두 개를 합친 Full Outer Join 총 3개가 있다.
- Outer Join은 조인하는 여러 테이블에서 한 쪽에는 데이터가 있고, 다른 쪽에는 데이터가 없는 경우 데이터가 있는 쪽 테이블의 내용을 모두 출력하는 것이다.
- 즉, 조건에 맞지 않아도 해당하는 행을 출력하고 싶을 때 사용할 수 있다.

- Outer Join은 두 테이블의 공통 영역을 포함해 한 쪽 테이블의 다른 데이터를 포함하는 조인방식이다.
- Left와 Outer를 정하는 기준은 FROM 절에 적은 테이블이 Left가 되고, JOIN 절에 적은 테이블이 Right가 된다.

<<<<<<< HEAD
- Left Join
	조인문의 왼쪽 테이블의 모든 결과를 가져온 후 오른쪽 테이블의 데이터를 매칭하고, 매칭되는 데이터가 없는 경우 NULL로 표시한다.
=======
- Left
	조인문의 왼쪽 테이블의 모든 결과를 가져온 후 오른쪽 테이블의 데이터를 매칭하고, 매칭되는 데이터가 없는 경우 NULL로 표시한다.
- Right
	조인문의 오른쪽 테이블의 모든 결과를 가져온 후 왼쪽 테이블의 데이터를 매칭하고, 매칭되는 데이터가 없는 경우 NULl로 표시한다.
- Full
	Left와 Right를 합친 것으로, 양쪽 모두 조건이 일치하지 않는 것까지 모두 결합해 출력한다. = 합집합
>>>>>>> 1b160f68c7b620f1fcb6ecfa1ab2f1a8c49dc467
