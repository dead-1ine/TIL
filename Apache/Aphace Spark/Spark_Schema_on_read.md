# Spark Schema on read

Spark에서 파일을 read할 때 불러올 파일의 스키마를 지정하여 지정된 컬럼만 가져오는 방식을 read on schema라고 한다.

Spark에서 파일을 read하기 전 schema를 선언하는 방식은 2가지 이다.

1. StructType 사용
2. DDL String 사용

개인적으로 DDL String이 StructType을 사용한 것보다 시각적 노이즈가 적어 가독성이 좋다고 생각한다.

### Spark의 Type 목록

------

| Data type             | Value type in Scala                                          | API to access or create a data type                          |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ByteType              | Byte                                                         | ByteType                                                     |
| ShortType             | Short                                                        | ShortType                                                    |
| IntegerType           | Int                                                          | IntegerType                                                  |
| LongType              | Long                                                         | LongType                                                     |
| FloatType             | Float                                                        | FloatType                                                    |
| DoubleType            | Double                                                       | DoubleType                                                   |
| DecimalType           | java.math.BigDecimal                                         | DecimalType                                                  |
| StringType            | String                                                       | StringType                                                   |
| BinaryType            | Array[Byte]                                                  | BinaryType                                                   |
| BooleanType           | Boolean                                                      | BooleanType                                                  |
| TimestampType         | java.sql.Timestamp                                           | TimestampType                                                |
| DateType              | java.sql.Date                                                | DateType                                                     |
| YearMonthIntervalType | java.time.Period                                             | YearMonthIntervalType                                        |
| DayTimeIntervalType   | java.time.Duration                                           | DayTimeIntervalType                                          |
| ArrayType             | scala.collection.Seq                                         | ArrayType(elementType, [containsNull])Note: The default value of containsNull is true. |
| MapType               | scala.collection.Map                                         | MapType(keyType, valueType, [valueContainsNull])Note: The default value of valueContainsNull is true. |
| StructType            | org.apache.spark.sql.Row                                     | StructType(fields)Note: fields is a Seq of StructFields. Also, two fields with the same name are not allowed. |
| StructField           | The value type in Scala of the data type of this field(For example, Int for a StructField with the data type IntegerType) | StructField(name, dataType, [nullable])Note: The default value of nullable is true. |

### Example. StructType

### Example. DDL String

### References

------

Spark Types: https://spark.apache.org/docs/latest/sql-ref-datatypes.html

Spark DDL String: https://stackoverflow.com/questions/71278455/spark-ddl-schema-json-struct