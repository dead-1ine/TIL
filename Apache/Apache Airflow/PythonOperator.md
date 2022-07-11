# PythonOperator

> 파이썬으로 작성한 코드를 실행한다.

```python
def print_context(ds, **kwargs):
    print(kwargs)
    print(ds)
    return 'Whatever you return gets printed in the logs'

run_this = PythonOperator(
	task_id='print_the_context',
    python_callable=print_context
)
```



- Python callable에 전달할 추가 Argument는 `op_args`와 `op_kwargs` 키워드를 사용한다.

```python
def my_sleeping_function(random_base):
    time.sleep(random_base)
    
for i in range(5):
    task = PythonOperator(
    	task_id='sleep_for_' + str(i),
        python_callable=my_sleeping_function,
        op_kwargs={'random_base': float(i) / 10}
    )
    
    run_this >> task
```

