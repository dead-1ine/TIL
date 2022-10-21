# xcom_pull

```python
from ... import PythonOperator

def get_num(a):
    return a + 10

get_num_task = PythonOperator(
	task_id='get_num_task',
    python_callable=get_num,
    op_args=[10],
    provide_context=True # task_instance에 return값을 등록하기 위한 method
    #provide context is for getting the TI (task instance ) parameters
)

num_b = "{{ task_instance.xcom_pull(task_id='get_num_task') }}"

plus_num_task = PythonOperator(
	task_id='plus_num_task',
    python_callable=lambda x: x + 100,
    op_args=[num_b]
)

get_num_task >> plus_num_task
```

