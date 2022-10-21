# Executor

Airflow에서 Executor는 Task가 실행되는 메커니즘으로, Executor를 어떻게 설정하느냐에 따라 Task의 실행방식이 달라진다. Task를 Worker에 어떻게 분배하여 작업을 진행시키느냐를 결정하는 부분이다.



Airflow에서 기본적으로 제공하는 Executor는 다음과 같다.

1. SequentialExecutor(Default)
2. LocalExecutor
3. CeleryExecutor
4. KubernetesExecutor



## Sequential Executor

Sequential Executor는 Airflow에서 제공하는 기본 Executor로, SQLite와 함께 사용할 수 있는 Executor이다. 하나의 Task만 실행할 수 있어 병렬성을 제공하지 않아 실제 운영환경에는 적합하지 않다.



## Local Executor

Local Executor는 Sequential Executor와 달리 병렬로 실행하는 것이 가능하며, 옵션을 통해 최대 몇 개의  Task를 병렬로 실행할지 설정할 수 있다. 

self.parallelism 옵션을 이용해 설정하며, 이 설정값을 0으로 설정하는 경우 Local Executor는 Task를 제한없이 무한으로 병렬 실행하게 되며 이를 Unlimited parallelism이라고 한다.



## Celery Executor

Celery Executor 역시 Local Executor와 마찬가지로 Task를 병렬로 실행할 수 있다. Celery는 추가적으로 Redis나 RabbitMQ와 같은 Message Queue가 추가적으로 필요한데 이는 Celery Executor가 클러스터  형식으로 구성되어 있고 MQ에 있는 Task를 실행하는 구조로 동작하기 떄문이다.

따라서, Celery Executor 클러스터 형식으로 구성할 수 있어 Executor에 대한 HA 구성과 Scale out이 자연스럽게 가능하며 Local Executor보다 실제 운영환경에 적합하다.

다만 DAG 파일 역시 Celery Executor로 사용하고 있는 모든 Worker에 배포되어야 하기 때문에 git을 이용해 DAG를 관리하고 배포하는 시스템을 구축해야 한다.