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
        
```

