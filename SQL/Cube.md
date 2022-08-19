# SQL - Cube

Cube함수는 항목들 간의 다차원적인 소계를 계산한다. ROLLUP과 달리 GROUP BY절에 명시한 모든 컬럼에 대해 소그룹 합계를 계산해준다.

```SQL
SELECT 
	product_id, month, SUM(amount) AS Amount
FROM 
	월별매출
GROUP BY 
	CUBE(product_id, month);
```

