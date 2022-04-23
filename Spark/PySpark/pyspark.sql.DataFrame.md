### Methods
---
agg(exprs)
	Aggregate on the entire DataFrame without groups

alias(alias)
	Returns a new DataFrame with an alias set.

approxQuantile(col, probabilities, relativeError)
	Calculates the approximate quantiles of numerical columns of a DataFrame

cache()
	Persists the DataFrame with the default storage level (MEMORY_AND_DISK).

checkpoint([eager])
	Returns a checkpointed version or this DataFrame
- Parameters:
	- eager : bool, optional
		Whether to checkpoint this DataFrame immediately

coalesce(numPartitions)
	Returns a new DataFrame that has exactly numPartitions partitions.
- Parameters:
	- numPartition : int
		specify the target number of partitions
- Example
	```python
	>>> df.coalesce(1).rdd.getNumberPartitions()
	1
	```

colRegex(colName)
	Selects column based on the column name specified as a regex and returns it as Column.

- Parameters:
	- colName : str
		string, column name specified as a regex
