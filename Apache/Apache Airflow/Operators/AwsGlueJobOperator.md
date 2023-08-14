in: apache-airflow-providers-amazon 2.4.0

amazon에서 만든 providers 2.4.0 버전에는 AwsGlueJobOperator, AwsGlueJobSensor 등이 있다.

우리 팀에서는 ETL 작업에 AWS Glue 서비스를 사용하는데, Airflow에서 AwsGlueJobOperator와 Sensor를 사용한다.

- AwsGlueJobOperator의 코드 
```python
class AwsGlueJobOperator(BaseOperator):
    
    template_fields = ('script_args',)
    template_ext = ()
    template_fields_renderers = {
        "script_args": "json",
        "create_job_kwargs": "json",
    }
    ui_color = '#ededed'

    def __init__(
        self,
        *,
        job_name: str = 'aws_glue_default_job',
        job_desc: str = 'AWS Glue Job with Airflow',
        script_location = Optional[str] = None,
        retry_limit: Optional[int] = None,
        num_of_dpus: int = 6,
        aws_conn_id: str = 'aws_default',
        region_name: Optional[str] = None,
        s3_bucket: Optional[str] = None,
        iam_role_name: Optional[str] = None,
        create_job_kwargs: Optional[dict] = None,
        run_job_kwargs: Optional[dict] = None,
        wait_for_completion: bool = True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.job_name = job_name 
        ...

    def execute(self, context):
        """
        Excutes AWS Glue Job from Airflow

        :return: the id of the current glue job.
        """
```
