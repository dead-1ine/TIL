# BashOperator

> Bash Shell 명령어를 실행한다.

```python
run_this = BashOperator(
    task_id='run_after_loop',
    bash_command='echo 1'
)
```



- Jinja Templates 사용

```python
also_run_this = BashOperator(
	task_id='also_run_this',
    bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"'
)
```



