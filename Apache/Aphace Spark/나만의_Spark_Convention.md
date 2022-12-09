# 나만의 Spark Coding Convention

1. import와 from - import 분리하기
2. external library와 internal library 분리하기
3. import 구간과 script 구간 줄바꿈 2
4. def 키워드 간 줄바꿈 2

```python
import pyspark

from pyspark.sql.functions import *

from custom_utils import get_s3_files

def main():
    # 전체 로직 플로우를 실행한다.
    amplitude_raw = extract_s3_amplitude_raw()
    amplitude_datetime = filter_datetime(amplitude_raw, '2022-12-09 00:00:00', '2022-12-10 00:00:00')
	load_to_s3(amplitude_datetime)

    
def extract_s3_amplitude_raw():
	return extracted_spark_df    
    

def filter_datetime(df, from_datetime, to_datetime):
    # filter logic
    return datetime_filtered_df


def load_to_s3(df, target_path):
    df.write.format('parquet').load(target_path)
    
    
if __name__=='__main__':
    main()
```