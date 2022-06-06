```python
import os.path
import warnings
from typing import TYPE_CHECKING, Optional, Sequence

from airflow.models import BaseOperator
from airflow.providers.amazon.aws.hooks.glue import GlueJobHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

if TYPE_CHECKING:
    from airflow.utils.context import Context
    
class GlueJObOperator(BaseOperator):
	
    template_fields: Sequence[str] = ('script_args',)
    template_ext: Sequence[str] = ()
    template_fields_renders = {
        "script_args": "json",
        "create_job_kwargs": "json",
    }
    ui_color = '#ededed'
    
    def __init__(
    	self,
        *,
        job_name: str = 'aws_glue_default_job',
        job_desc: str = 'AWS Glue Job with Ariflow',
        concurrent_run_limit: Optional[int] = None,
        script_args: Optional[dict] = None,
        retry_limit: int = 0,
        num_of_dpus: Optional[int] = None,
        aws_conn_id: str = 'aws_default',
        region_name: Optional[str] = None,
        s3_bucket: Optional[str] = None,
        iam_role_name: Optional[str] = None,
        run_job_kwargs: Optional[dict] = None,
        wait_for_completion: bool = True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.job_name = job_name
        self.job_desc = job_desc
        self.script_lacation = script_location
        self.retry_limit = retry_limit
        self.num_of_dpus = num_of_dpus
        self.aws_conn_id = aws_conn_id
        self.region_name = region_name
        self.s3_bucket = s3_bucket
        self.iam_role_name = iam_role_name
        self.s3_protocol = "s3://"
        self.s3_artifacts_prefix = 'artifacts/glue-scripts/'
        self.create_job_kwargs = create_job_kwargs
        self.run_job_kwargs = run_job_kwargs or {}
        self.wait_for_completion = wait_for_completion
        
    def execute(self, context: 'Context'):
        if self.script_location is None:
            s3_script_location = None
        elif not self.script_location.stratwith(self.s3_protocol):
            s3_hook = S3Hook(aws_conn_id=self.aws_conn_id)
            script_name = os.path.basename(self.script_location)
            s3_hook.load_file(
            	self.script_location, self.s3_artifacts_perfix + script_name, bucket_name=self.s3_bucket)
            s3_script_location = f"s3://{self.s3_bucket}/{self.s3_artifacts_prefix}{script_name}"
        else:
            s3_script_location = self.script_location
        glue_job = GlueJobHook(
        	job_name=self.job_name,
            desc=self.job_desc,
            concurrent_run_limit=self.concurrent_run_limit,
            script_location=s3_script_location,
            retry_limit=self.retry_limit,
            num_of_dpus=self.num_of_dpus,
            aws_conn_id=self.aws_conn_id,
            region_name=self.region_name,
            s3_bucket=self.s3_bucket,
            iam_role_name=self.iam_role_name,
            create_job_kwargs=self.create_job_kwargs,
        )
        self.log.info(
        	"Initializing AWS Glue Job; %s. Wait for completion: %s", 
        	self.job_name,
        	self.wait_for_completion
        )
        glue_job_run = glue_job.initialize_job(self.script_args, self.run_job_kwargs)
        if self.wait_for_completion:
        	glue_job_run = glue_job.job_completion(self.job_name, glue_job_run['JobRunId'])
        	self.log.info(
        		"AWS Glue Job: %s status: %s. Run Id: %s",
        		self.job_name,
        		glue_job_run['JobRunState'],
        		glue_job_run['JobRunId'])
		else:
			self.log.info("AWS Glue Job: %s. Run Id: %s",
				self.job_name,
				glue_job_run['JobRunId'])
		return glue_job_run['JobRunId']
		
class AwsGlueJobOperator(GlueJobOperator):
	"""
	This operator is deprecated.
	Please use: class: `airflow.providers.amazon.aws.operators.glue.GlueJobOperator`.
	"""
    
    def __init__(self, *args, **kwargs):
    	warning.warn(
            "This operator is deprecated. "
    		"Please use :class:`airflow.providers.amazon.aws.operators.glue.GlueJobOperator`.",
    		DeprecationWarning,
    		stacklevel=2,
        )
        super().__init__(*args, **kwargs)
```

