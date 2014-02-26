import os.path

import tcprepl
import BigWorld

def echo(s):
    if tcprepl.write_client is not None:
        tcprepl.write_client(s)

def exec_file(filename, exec_globals=None):
    if exec_globals is None:
        exec_globals = {}

    if not os.path.isfile(filename):
        filename = BigWorld.wg_resolveFileName(filename)

    with open(filename, 'r') as f:
        code = f.read()

    exec code in exec_globals
