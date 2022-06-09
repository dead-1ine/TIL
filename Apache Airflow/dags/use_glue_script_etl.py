import time
import boto3

from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator

glue_client = boto3.client('glue', region_name='ap-northeast-2')

dag = DAG(dag_id="ad-raw-impression-ctr-etl-dag",
          default_args=dict(
              owner="yangws",
              start_date=datetime(2022, 5, 27, 14, 5, 0) - timedelta(hours=9),
          ),
          max_active_runs=10,
          schedule_interval="*/5 * * * *")


def glue_job(job_name, execution_date):
    response = glue_client.start_job_run(
        JobName=job_name,
        Arguments={
            '--execution_date': execution_date,
        },
        Timeout=4880)
    print(f" job run id : {response}")


def operator(task_id, depends_on_past=False):
    return PythonOperator(
        task_id=task_id,
        python_callable=glue_job,
        op_kwargs=dict(
            job_name=task_id,
            execution_date='{{execution_date.strftime("%Y-%m-%d %H:%M:%S")}}'
        ),
        depends_on_past=depends_on_past,
        dag=dag)


def task(task_id, depends_on_past=False, seconds=10):
    task_operator = operator(task_id, depends_on_past)
    task_operator.post_execute = lambda **x: time.sleep(seconds)
    return task_operator


task("ad-v2-impression-ctr-etl")