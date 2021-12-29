### Pivot Table 함수의 구성요소

---

- 행 인덱스
- 열 인덱스
- 데이터 값
- 데이터 집계함수

```python
pdf1 = pd.pivot_table(df, 
                     index='class',
                     columns='sex',
                     values='age',
                     aggfunc='mean')
```

