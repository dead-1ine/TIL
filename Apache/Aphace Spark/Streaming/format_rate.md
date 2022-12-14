# Spark Streaming rate format



### Step 1: Reading JSON Files from Directory

```scala
import org.apache.spark.sql.{SparkSession}
import org.apache.spark.sql.functions._

// Create Spark Session
val spark = SparkSession.builder()
	.master("local")
	.appName("Rate Source")
	.getOrCreate()

val df = spark.readStream
	.format("rate")
	.option("rowPerSecond", 3)
	.load()

df.printSchema()
println("Streaming DataFrame: " + df.isStreaming)
```



### Step 2: Basic transformation and output to the console

```scala
var final_df = df.withColumn("result", col("value") + lit(1))
final_df.printSchema()

final_df.writeStream
	.format("console")
	.outputMode("append")
	.start()
	.awaitTermination()
```



```scala
import org.apache.spark.sql.streaming._

var final_df = df.select("value").groupBy("value").count()

final_df.printSchema()

final_df.writeStream
	.format("console")
	.outputMode("complete")
	.option("truncate", false)
	.start()
	.awaitTermination()
```

