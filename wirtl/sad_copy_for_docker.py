import tempfile, shutil, os

def create_temporary_copy(path):
  dirname, basename = os.path.split(path)
  tmp = tempfile.NamedTemporaryFile(dir="abomination/wirtle/dockerplace/", prefix=basename, suffix="")
  shutil.copy2(path, tmp.name)
  return tmp
