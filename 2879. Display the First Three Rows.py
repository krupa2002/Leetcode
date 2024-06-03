# Understanding
''' pd.head(3)- .head() is a approach to find out the no of rows from begining and tail is for finding ending rows '''

#Code
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
