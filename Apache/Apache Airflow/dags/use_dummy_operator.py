import time
import boto3

from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator

from utils.exception import GlueJobStatusNotFoundError

jdbc_url_dev = Variable.get('ad_rds_url_dev')
rds_user_dev = Variable.get('ad_rds_user_dev')
rds_password_dev = Variable.get('ad_rds_password_dev')

docdb_catalog_url_dev = Variable.get('ad_docdb_catalog_url_dev')
docdb_catalog_user_dev = Variable.get('ad_docdb_catalog_user_dev')
docdb_catalog_password_dev = Variable.get('ad_docdb_catalog_password_dev')

glue_client = boto3.client('glue', region_name='ap-northeast-2')

dag = DAG(dag_id="ad-scoring-dag",
          default_args=dict(
              owner="yangws",
              start_date=datetime(2022, 6, 10, 8, 0, 0) - timedelta(hours=9)
          ),
          catchup=True,
          max_active_runs=15,
          schedule_interval="*/15 * * * *")


def observe_glue_job_state(job_name, run_id):
    print(job_name, "run_id : " + run_id)
    while True:
        time.sleep(3)
        job_run = glue_client.get_job_run(JobName=job_name, RunId=run_id)
        job_run_state = job_run['JobRun']['JobRunState']
        if job_run_state != 'RUNNING':
            break

    if job_run_state == "SUCCEEDED":
        print(job_name, "job_run_state : " + "Succeeded")
    else:
        print(job_name, "job_run_state : " + "*Prod* Failed")
        raise GlueJobStatusNotFoundError(job_run_state)


def glue_job(job_name, execution_date):
    response = glue_client.start_job_run(
        JobName=job_name,
        Arguments={
            '--execution_date': execution_date,
            '--jdbc_url': jdbc_url_dev,
            '--user': rds_user_dev,
            '--password': rds_password_dev,
            '--docdb_catalog_url_dev': docdb_catalog_url_dev,
            '--docdb_catalog_user_dev': docdb_catalog_user_dev,
            '--docdb_catalog_password_dev': docdb_catalog_password_dev,
        },
        Timeout=4880)
    job_run_id = response['JobRunId']
    print(f"--- job name: {job_name}")
    print(f"--- job run id: {job_run_id}")
    observe_glue_job_state(job_name, job_run_id)


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


def dummy(task_id):
    return DummyOperator(task_id=task_id,
                         depends_on_past=False,
                         trigger_rule="all_success",
                         dag=dag)


def task(task_id, depends_on_past=False, seconds=10):
    task_operator = operator(task_id, depends_on_past)
    task_operator.post_execute = lambda **x: time.sleep(seconds)
    return task_operator


(
    dummy("start_extract_ctrs") >>
    [task("ad-v2-ctr-24h2h-per15"), task("ad-v2-ctr-168h-per15")] >>
    dummy("end_extract_ctrs") >>
    task("ad-v2-scoring") >>
    task("ad-v2-product-grade-uploader")
)