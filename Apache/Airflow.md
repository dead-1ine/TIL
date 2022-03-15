### 개요

---

Airflow는 복잡한 워크플로우를 프로그래밍 방식으로 작성해서, 스케줄링하고 모니터링할 수 있는 플랫폼이다.

Airflow에는 서로에 대한 의존성을 표현할 수 있고, 스크립트가 실패했을 때 알림을 보내 확인하고 쉽게 수정 후 재시도할 수 있고, 이전 날짜 작업이 실패했을 때 그 날짜만 다시 실행하는 등 위 문제점을 많이 해결해준다.



### 개념

---

- DAG(Directed Acyclic Graph)
- DAG는 유향 비순환 그래프라고 하며 에어플로우의 워크플로우는 Python을 사용하여 작성할 수 있다.
- 하나의 DAG 안에는 한 개 이상의 Task가 있으며, Task는 실제 작업을 실행시키는 것이다.



- DAG 스크립티의 예시

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from utils.alert import on_failure, on_success

default_args = {
  'owner': 'airflow',
  'catchup': False,
  'execution_timeout': timedelta(hours=6),
  'depends_on_past': False,
  'on_failure_callback': on_failure,
  'on_success_callback': on_success
}

dag = DAG(
  'sample_dag',
  default_args = default_args,
  description = "sample Description",
  schedule_interval = "0 16 * * *",
  start_date = days_ago(2),
  tags = ['daily'],
  max_active_runs = 3,
  concurrency = 1
)

sample_task = BashOperator(
	task_id = "Sample_Task",
  bash_command = 'python3 sample_task.py',
  dag = dag
)
```





참고 사이트: https://data-engineer-tech.tistory.com/30