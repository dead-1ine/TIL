# **context

Airflow DAG에서 PythonOperator를 실행할 때 해당 함수에 Airflow Context 변수를 parameter로 전달한다.



- Airflow Context 변수들은 아래와 같은 키워드 인자 형태로 전달된다.

```python
get_data(conf=..., dag=..., dag_run=..., execution_date=...)
```



PythonOperator가 실행될 때 전달받는 Context 변수들을 사용하는 방법은 두 가지이다.

1. **kwargs로 Context 변수들을 Dictionary 형태로 전달받기
2. 전달받을 Context 변수를 명시적으로 선언하여 전달받기



- **kargs로 Context 변수들을 Dictionary 형태로 전달받기

```python
# **kwargs 인자를 통해 Airflow가 자동으로 전달하는 Context를 변수들을 사용한다는 것을 표현함
def get_data(**kwargs):
    print(kwargs['prev_ds'])
    print(kwargs['ds'])
    print(kwargs['next_ds'])
    
# Airflow는 Task 실행 시 각 Context 변수들을 위에서 얘기한 키워드 인자 형태로 전달함
get_data()
# 2022-07-19
# 2022-07-20
# 2022-07-21
```



- 전달받을 Context 변수를 명시적으로 선언하여 전달받기

```python
def get_execution_date(execution_date, **kwargs):
    print(execution_date)
    print(kwargs['ds'])
    
get_execution_date() # 사용자가 Parameter를 전달하지 않아도 Airflow가 자동으로 각 변수들을 전달함
# 2022-07-20 00:00:00
# 2022-07-20
```

