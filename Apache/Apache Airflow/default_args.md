# Airflow - Default Args

> 이 글은 Airflow 2.2.2 버전을 기준으로 작성한 글이다.

Airflow DAG의 default_args 키워드 인자는 dict 형태의 파라미터를 전달받는다. 전달받은 각 dict의 Key는 Value에 따라 다양한 기능으로 동작한다.

이 글은 각 Key별 Value에 따른 기능 동작에 대한 설명을 정리한 글이다.



## owner(str)

> 해당 DAG의 소유자, 닉네임으로 설정이 가능하지만 OS의 사용자 이름이나 airflow 내의 계정 이름으로 설정할 것을 추천

## depends_on_past(bool)

> 

## email(str or list[str])

> 사용자의 email을 등록하는 인자
>
> `{'email': ['user@email']}`

## email_on_failure(bool)

> Dag의 task가 failed되면 등록된 email로 Dag의 context를 보내는 여부를 결정
>
> `{'email_onfailure': True}`

## email_on_retry(bool)

> Dag의 task가 재시도될 경우 메일을 보내는 여부를 결정
>
> `{'email_on_retry': True}`

## retries(int)

> task가 실패할 경우 재시도할 횟수
>
> `{'retries': 3}`

## retry_delay(datetime.timedelta)

> 재시도 간의 delay 시간
>
> `{'retry_delay': timedelta(minutes=1)}`

## queue

> which queue to target when running this job. Not all executors implement queue management, the CeleryExecutor does support targeting specific queues.

## pool

> the slot pool this task should run in, slot pools are a way to limit concurrency for certain tasks

## pool slot

> the number of pool slots this task should use (>= 1) Values less than 1 are not allowed

## priority_weight

## dag

## sla

## execution_timeout

> max time allowed for execution of this task instance, if it goes beyond it will raise and fail.

## on_failure_callback

## on_success_callback

## on_retry_callback

## sla_miss_callback

## trigger_rule



## Task에 대한 우선순위 룰

1. 명시적으로 전달된 Operator의 arguments
2. dict 형태로 미리 선언한 default_args의 값
3. 해당 Operator의 default value



## Templating with Jinja

