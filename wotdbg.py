import os.path

import tcprepl
import BigWorld

def echo(s):
    '''Send string to client'''
    if tcprepl.write_client is not None:
        tcprepl.write_client(s)

def exec_file(filename, exec_globals=None):
    '''
    Execute file

    Try to find file named `filename` and execute it. If `exec_globals` is
    specified it is used as globals-dict in exec context.
    '''
    if exec_globals is None:
        exec_globals = {}

    if not os.path.isfile(filename):
        filename = BigWorld.wg_resolveFileName(filename)

    with open(filename, 'r') as f:
        code = f.read()

    exec code in exec_globals
