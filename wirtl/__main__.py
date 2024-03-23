import tempfile
import pathlib
import shutil

import fire
import docker

class YouWroteBadCodeDude(Exception): pass

from . import python
from .manifest import manifest, dbtRunner
from .hashmagic import is_itself_or_local_imports_changed
from .sad_copy_for_docker import create_temporary_copy

def run():
    # execute an entire dbt run but container python
    for result in manifest:
        if result.node.language == 'sql':
            # todo not use dbt as the runner
            dbtRunner().invoke(['run', '-m', result.node.name])
        elif result.node.language == 'python':
            path = pathlib.Path(result.compiled_path)
            #todo containers (requirements.txt)
            #todo containers (full on arbitrary container)
            python.local_run(result.name, result.compiled_path)
        else:
            raise YouWroteBadCodeDude

fire.Fire()
