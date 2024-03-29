# custom_operator

Airflow의 모든 오퍼레이터는 `BaseOperator`클래스의 서브 클래스로 만들어야 한다.



- 커스텀 오퍼레이터의 베이스 코드

```python
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class CustomOperator(BaseOperator):
    
    @apply_defaults # 기본 DAG 인수를 커스텀 오퍼레이터에게 전달하기 위한 데코레이터
    def __init__(self, conn_id, **kwargs): # BaseOperator 생성자에게 추가 키워드 인수를 전달
    	super.__init__(self, **kwargs)
        self._conn_id = conn_id
        ...
```



- 오퍼레이터에 기본 인수 적용

​	DAG의 default_args로 지정한 dict 값을 CustomOperator에 전달하기 위해서는 `@apply_defaults`라는 데코레이터를 사용한다. 이 데코레이터는 CustomOperator의 ``__init__()``에 적용된다. 
​	결론적으로, CustomOperator의 `__init__()`에 `@apply_default`를 사용하지 않으면 DAG의 `default_args` 인자를 전달받을 수 없다.

```python
default_args = {
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
	...
    default_args=default_args
) as dag:
    CustomOperator(
    	...
    )
```



오퍼레이터가 실제로 작업해야 하는 사항은 `execute()`로 구현한다. 이 메서드는 Airflow가 DAG를 실행할 때 DAG 안에서 실행되는 오퍼레이터의 메인 메서드가 된다.

- 오퍼레이터의 execute 메서드

```python
class CustomOperator(BaseOperator):
    ...
    def execute(self, context): # DAG에서 CustomOperator로 정의한 Task가 실행될 때 호출되는 메인 메서드
    ...
```

위 리스트와 같이 `execute()` 는 `context`라는 하나의 파라미터만을 받으며, 이 파라미터는 Airflow의 모든 Context Variable을 담고 있는 `dict` 객체이다. `execute()`는 Airflow의 Context Variables를 이 파라미터에서 참조하여 해당 오퍼레이터가 수행해야 하는 작업을 수행한다.



BaseOperator에서 기본적으로 사용하는 변수들 외에 다른 파라미터를 전달받고 싶다면 CustomOperator의 `__init__()`에 전달받을 파라미터로 작성하면 된다.

- 커스텀 오퍼레이터 기본 구현하기

```python
Class CustomOperator(BaseOperator):
    
    @apply_defaults
    def __init__(
        self, conn_id, output_path, start_date, end_date, **kwargs
    ):
        super(CustomOperator, self).__init__(**kwargs)
        
        self._conn_id = conn_id
        self._output_path = output_path
        self._start_date = start_date
        self._end_date = end_date
    
    def execute(self, context):
        ...
        self.log.info("BaseOperator는 log객체를 가지고 있다.")
        ...
```



로깅이 필요할 때는 BaseOperator에서 제공하는 `logger`를 사용하면 된다. 이 `logger`는 `self.log` 속성으로 사용할 수 있다.



- CustomOperator 사용 예제

```python
run_custom_task = CustomOperator(
	task_id='run_custom_task',
    conn_id='connection_id',
    start_date='2022-09-01',
    end_date='2022-09-02',
    output_path='/data/2022-09-01.json'
)
```

이 구현의 단점은 오퍼레이터가 execute될 때 시작/종료 날짜를 직접 지정해야 한다는 것이다. 즉, 오퍼레이터는 DAG의 실행 날짜에 관계없이 하드코딩된 날짜 기간에 대한 데이터를 가져온다는 것이다.

다행히 Airflow에서는 템플릿 가능한 오퍼레이터 변수를 만들 수 있다. 이를 통해 실행 날짜와 같은 Context Variables를 참조할 수 있다. 특정 인스턴스 변수를 템플릿으로 만들려면, `templates_fields` 클래스 변수에 해당 변수명을 지정하여 Airflow에 알려줘야 한다.

- Add templates_fields

```python
class CustomOperator(BaseOperator):
    ...
    templates_fields = ('_start_date', '_end_date', '_output_path') # CustomOperator에서 템플릿화할 인스턴스 변수들을 Airflow에 알려준다.
    ...
    @apply_defaults
    def __init__(
    	self,
        conn_id,
        output_path,
        start_date="{{ ds }}", # 기본값을 지정한 것
        end_date="{{ next_ds }}", # 기본값을 지정한 것
        **kwargs,
    ):
        super(CustomOperator, self).__init__(**kwargs)
        
        self._conn_id = conn_id
        self._output_path = output_paths
        self._start_date = start_date
        self._end_date = end_date
```



위와 같은 방식으로 변수` _start_date, _end_date, _output_path` (이 변수들은 `__inint__` 안에서 생성된다.)가 템플릿으로 가능하다고 Airflow에 전달할 수 있다. 

만약 문자열 파라미터에 Jinja Template(`{{ }}`)을 사용하면, Airflow는 `execute`메서드를 호출하기 전에 이 값들을 템플릿화한다. 그 결과 다음 리스트와 같이 템플릿화된 인수를 사용하는 오퍼레이터를 사용할 수 있다.



- 오퍼레이터에서 템플릿 사용하기

```python
from custom.operators import CustomOperator

run_custom_task = CustomOperator(
	task_id='run_custom_task',
    conn_id='connection_id',
    start_date="{{ ds }}",
    end_date="{{ next_ds }}",
    output_path="/data/custom_operator/{{ ds }}.json"
)
```

위 코드를 실행하면 Airflow는 `start_date, end_date, output_path`에 전달된 Jinja Template 형태로 감싸진 ds, next_ds로 값을 채우게 된다.