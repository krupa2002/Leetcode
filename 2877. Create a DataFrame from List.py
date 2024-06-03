import pandas as pd #importing pandas library

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id","age"])

#Defining function name createDataframe
#student_data takes the arugument
#List[List[int]])- student_data should be a 2D list where each sublist contains integers.
#-> pd.DataFrame:  - return type
#return - its returns newly created dataframe
#student_data,columns=["student_id","age"] - we are taking the dataframe and from that we are considering only 2 columns.
