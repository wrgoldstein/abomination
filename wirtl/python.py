import importlib.util
import pandas as pd
import psycopg2

# is it even worth commenting "todo"?
con = psycopg2.connect(database="jaffle_shop")


class ICanCallRef:
    @staticmethod
    def ref(table):
        "table fetcher to pass to python function"
        "eventually to inject tables into the container"
        # nb make this incremental when needed
        sql = f"select * from dbt_wrgoldstein.{table}"
        return pd.read_sql(sql, con)


def local_run(name, compiled_path):
    "`result` is the output of a `dbt compile`"
    spec = importlib.util.spec_from_file_location(name, compiled_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    session = None # I think this should be the `con` actually..?
    df = mod.model(ICanCallRef, session)
    df.to_sql(name, con, if_exists="replace") 

