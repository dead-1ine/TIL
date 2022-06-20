import pyspark

from pyspark.sql.functions import col, min, max

def print_min_max(self, col_name: str):
    
    # TODO: Pyspark 객체 확인 시 Type
    if type(self) != pyspark.dataframe:
        raise TypeError
    
    print(self.select(min(col(col_name)), max(col(col_name))).show(1, False))

# 