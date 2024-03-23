from dbt.cli.main import dbtRunner, dbtRunnerResult
from dbt.contracts.graph.manifest import Manifest

# use 'parse' command to load a Manifest

parsed: dbtRunnerResult = dbtRunner().invoke(["parse"])

# nb "compile" alone also parses, this does it in two steps
# just to show its possible, maybe the intermediate parse is useful
compiled: dbtRunnerResult = dbtRunner(parsed.result).invoke(["compile"])
manifest: Manifest = compiled.result
