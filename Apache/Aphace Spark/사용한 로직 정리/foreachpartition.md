# repartition(n).foreachPartition(func(f"{TaskContext.get().partitionId()}))



- repartition
- foreachPartition
- lambda
- TaskContext
    - get
    - partitionId



```python
result.repartition(16).foreachPartition(lambda x: pd.DataFrame(x).to_csv(s3_out_path + file_name + f"{TaskContext.get().partitionId()}.csv", header=True, index=False))
```

