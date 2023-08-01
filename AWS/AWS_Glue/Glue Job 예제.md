# Glue Job: Spark Script

현재 저희 팀에서는 AWS에서 모든 개발을 진행합니다. 그 중 ETL 작업을 위해 주로 사용되는 AWS Glue의 여러 서비스 중에서 Job --Spark Script를 어떠한 형태로 사용하는지 간략히 작성하여 공유하기 위해 이 글을 씁니다.

Glue Job의 구성 요소는 크게 네 가지입니다.

1. `getResolvedOptions()`를 사용하여 Glue Job이 실행될 때 전달받은 인자를 분석
2. ETL 작업을 수행하는 `main()` 생성
3. `main()` 내부에서 수행될 함수들을 뒤에서 선언
4. Python의 `if __name__ == '__main__'` 구문을 통한 `main()` 실행



### 1. `getResovledOptions()`

Glue Job은 외부에서 Triggering되어 실행됩니다. 저는 현재 AWS MWAA를 사용하여 특정 작업 스케줄링에 따라 Job을 Triggering하며, 이 때 boto3가 wrapping된 GlueJobOperator의 인자로 Glue Job에서 쓰일 인자들을 전달합니다. (이 글을 읽는 독자가 Airflow Operator까지 알아야 할까?)

```python
import sys
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, [
    'first_arg',
    'second_arg',
    ...
])

first_arg = args['first_arg']
second_arg = args['second_arg']
```

