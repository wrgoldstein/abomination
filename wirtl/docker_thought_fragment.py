
            t = create_temporary_copy(path)
            if is_itself_or_local_imports_changed(path):
                # build docker container

                td = tempfile.TemporaryDirectory()
                
                # copy the python model code (this is nasty)
                # it can be done much less nastily
                grossness = f"""
##################### this would be the model code, with a `model/2` function
{code}

###################### copied from `./python.py`
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
        sql = f"select * from dbt_wrgoldstein.{{table}}"
        return pd.read_sql(sql, con)

name = {name}
spec = importlib.util.spec_from_file_location(name, compiled_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
session = None # I think this should be the `con` actually..?
df = model(ICanCallRef, session)
df.to_sql(name, con, if_exists="replace") 
"""
                entrypoint = pathlib.Path(td.name) / 'entrypoint.py'
                entrypoint.write_text(grossness)

                # copy the dockerfile
                shutil.copy2("wirtl/Dockerfile.python_default", td.name + '/Dockerfile')
                client = docker.from_env()
                client.images.build(
                    path=td.name,
                )
                client.images.run
