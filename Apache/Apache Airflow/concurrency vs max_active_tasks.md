# Airflow - DAG's Param concurrency vs max_active_tasks

`concurrency`와 `max_active_tasks`는 둘 다 Airflow에서 동시에 실행되는 Task 수를 제한하는데 사용되지만, 두 매개변수는 서로 다른 범위에서 적용됩니다. 

1. `concurrency`: 이 매개변수는 특정 DAG에 대해 동시에 실행할 수 있는 Task 수를 제한합니다. 예를 들어, `concurrency=1`로 설정하면 해당 DAG 내에서 한 번에 하나의 Task만 실행할 수 있습니다. 이 값이 높으면 여러 Task가 동시에 실행될 수 있습니다.
2. `max_active_tasks`: 이 매개변수는 전체 Airflow 인스턴스에 대해 동시에 실행할 수 있는 Task 수를 제한합니다. 이는 모든 DAG에서 실행되는 Task의 총 수를 제한하는 데 사용됩니다. `airflow.csg`파일에서 `core` 섹션의 `max_active_tasks_per_dag` 설정으로 이 값을 조정할 수 있습니다.

요약하면, `concurrency`는 특정 DAG의 동시 실행 Task 수를 제한하는 반면, `max_active_tasks`는 전체 Airflow 인스턴스에서 동시 실행되는 Task 수를 제한합니다.