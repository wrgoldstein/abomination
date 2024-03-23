import requests
import pandas as pd

from pandas import DataFrame

from ...macros.my_py_func import printprinter

def model(dbt, session):
    printprinter()
    requests.get("https://google.com")
    df = dbt.ref('my_first_dbt_model')
    print("hello from inside a python function")
    print("here's an input")
    print(df)
    return pd.DataFrame([{"a": 1}])
