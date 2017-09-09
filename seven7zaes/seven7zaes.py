# -*- coding: utf-8 -*-

"""Main module."""

from pathlib import Path
import subprocess


p = Path(os.getenv('USERPROFILE') + r'\Pictures\N')
method = Path(os.getenv('ProgramFiles') + r'\7-zip')

cwd = Path(os.getenv('TEMP') + r'\work')

try:
    os.mkdir(cwd)
except FileExistsError as err:
    print(err)

parent = (dn for dn in p.glob('*') if dn.is_file() is False)

def get_dirs(path):
    dn = ''
    for dn in path.glob('*'):
        if dn.name != dn.parent.name:
            return (dn.parent.name, dn.parent)
        else:
            return get_dirs(dn)
    return None

dirs = (get_dirs(dn) for dn in parent)

def compress(name, src, cwd, method, password):

    cmd = ['7z', 'a', name,
       r'-r', '-p' + password, '-mhe', src + r'\*']

    env = {"PATH": r'C:\Program Files\7-Zip'}

    return subprocess.run(cmd, cwd=cwd, shell=True, env=env,
               stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for name, src in dirs:
    result = compress(name, str(src.absolute()), cwd, method)
#     print(result.args)
    print(result.stderr.decode() or None)

