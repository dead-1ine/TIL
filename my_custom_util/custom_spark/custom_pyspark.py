import pyspark
from pyspark.sql.dataframe import DataFrame

from pyspark.sql.functions import col, min, max

def print_min_max(self, col_name: str):
    
    if type(self) != DataFrame:
        raise TypeError
    
    print(self.select(min(col(col_name)), max(col(col_name))).show(1, False))