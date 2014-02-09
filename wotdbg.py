import tcprepl

import BigWorld

def echo(s):
    if tcprepl.write_client is not None:
        tcprepl.write_client(s)

def player():
    return BigWorld.player()

