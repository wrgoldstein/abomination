"""
Shouldn't have spent the time I was just curious if I
could solve this little piece of checking for changed
files while thinking about Dockerizing.
"""

import ast
import hashlib
import pathlib


def read_pypath(pypath):
    return pathlib.Path("/".join(pypath.split("."))).with_suffix(".py").read_text()

def hash_source_and_local_imports(path):
    source = path.read_text()
    tree = ast.parse(source)

    imported_pypaths = [
        x.module for x in tree.body if type(x) == ast.ImportFrom and x.module.startswith('macros')
    ]

    bigstr = "".join([read_pypath(p) for p in imported_pypaths] + [source])
    return hashlib.md5(bigstr.encode()).hexdigest()

def is_itself_or_local_imports_changed(path):
    hash = hash_source_and_local_imports(path)
    # todo maybe needs more of the path idk
    hash_file = pathlib.Path("wirtl/hashes") / path.name

    if hash_file.exists() and hash_file.read_text() == hash:
        return False
    
    hash_file.write_text(hash)
    return True
