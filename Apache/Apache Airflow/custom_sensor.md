# custom_sensor

센서는 특별한 유형의 오퍼레이터이다. 일반적인 사용법은 DAG 안에서 다운스트림 태스크를 실행하기 전에 특정 조건이 충족될 때까지 대기하는 것이다.

센서는 오퍼레이터와 매우 유사하고 `BaseOperator` 대신 `BaseSensorOperator` 클래스를 상속한다.



- 커스텀 센서의 베이스 코드

```python
from airflow.sensors.base import BaseSensorOperator

class CustomSensor(BaseSensorOperator):
    ...
```



 `BaseSensorOperator`는 센서에 대한 기본 기능을 제공하고, 오퍼레이터의 `execute()` 대신 `poke()`를 구현해야 한다.

- 센서의 `poke()`

```python
class CustomSensor(BaseSensroOperator):
    
    def poke(self, context):
        ...
```



Airflow가 콘텍스트를 포함하는 단일 인수만을 사용하는 측면에서 센서의 `poke()`와 오퍼레이터의 `execute()`는 매우 유사하다. 하지만 `execute()`와는 다르게 `poke()`는 `Boolean`을 반환하는데, 이 값은 센서 상태를 `True/False`로 나타낸다.  상태가 `False`이면 센서가 상태를 다시 체크할 때까지 몇 초 정도 대기 상태로 들어간다. 이 프로세스는 상태 값이 `True`가 되거나 타임 아웃될 때까지 반복되며, 센서가 실행을 끝내고 `True`를 반환하면 다운스트림 태스크를 시작한다.



- 센서 클래스의 기본 구현ㄴ

```python
from airflow.sensors.base import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

class CustomSensor(BaseSensorOperator):
    """
    Sensor that waits for the custom_job
    """
    # 센서가 오퍼레이터의 특정한 유형이기에 오퍼레이터를 구현할 때 사용했던 것과 같은 설정을 사용한다.
    template_fields = ("_startt_date", "_end_date")
    
    @apply_defaults
    def __init__(
        self, 
        conn_id, 
        start_date="{{ ds }}",
        end_date="{{ next_ds }}",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self._start_date = start_date
        self._end_date = end_date
```



생성자를 만든 후에는 `poke()`를 구현하기만 하면 된다.  이 메서드는 단순히 주어진 시작/종료 날짜 사이에 데이터가 있는지 체크하는 것이며, 날짜 사이에 레코드가 있다면 `True`를 반환한다. 이를 위해 모든 데이터 레코드를 전부 가져올 필요는 없으며, 해당 범위에 적어도 한 개의 레코드가 존재하는지 체크하면 된다.

Hook를 사용하면 위 내용을 구현하기 매우 단순해진다. 여기에서는 적어도 하나 이상의 레코드가 있는지 확인하면 되기 때문에 `get_records()`에서 반환되는 제너레이터에서 `next()`를 호출하여 제너레이터가 빈 값일 경우 `StopIteration` 오류를 발생시킨다. 따라서 `try/except`를 사용하여 예외 사항을 체크하고, 예외가 발생하지 않으면 `True`를, 그렇지 않으면 `False`를 반환한다.

- `poke()` 구현하기

```python
class CustomSensor(BaseSensorOperator):
    ...
    def poke(self, context):
        hook = CustomHook(self._conn_id)
        
        try:
            next( # 훅에서 레코드 하나를 가져오는 것을 시도
                hook.get_records(
                    start_date=self._start_date,
                    end_date=self._end_date,
                    batch_size=1
                )
            )
            self.log.info(f"Found records for {self._start_date} to {self._end_date}")
            return True # next가 성공이면 적어도 하나의 레코드가 있으므로 True
        except StopIteration: # next가 실패하면 레코드 콜렉션이 비어있으므로 False
            self.log.info(
                f"Didn't find any records for {self._start_date} "
                f"to {self._end_date}, waiting..."
            )
            return False
        finally:
            hook.close()
```

