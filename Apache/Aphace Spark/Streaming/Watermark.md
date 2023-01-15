# Watermark

워터마크는 이벤트가 너무 늦게 들어오거나 등의 이벤트를 기다리는 시간을 결정하는 임곗값이다. 워터마크를 벗어난 것으로 간주되는 이벤트는 폐기된다.

```scala
val timeStampEvents = raw
	.withColumn("timestamp", $"ts".cast(TimestampType))
	.withWatermark("timestmap", "5 minutes")
```



```scala
import spark.implicits._

val words = ... // streaming DataFrame of schema { timestamp: Timestamp, word: String }

// Group the data by window and word and compute the count of each group
val windowedCounts = words
	.withWatermark("timestamp", "10 minutes")
	.groupBy(
    	window($"timestamp", "10 minutes", "5 mintues"),
    	$"word")
	.count()
```