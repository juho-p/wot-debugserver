#!/usr/bin/python

import socket
import threading
import readline

HOST = '127.0.0.1'
PORT = 2222

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

stream = socket.makefile()

newline = '\r\n'
readymsg = '~~~ok!~~~'

def write_stream(msg):
    stream.write(msg + newline)
    stream.flush()

def exec_sync(cmd):
    write_stream(cmd)
    result = []
    for line in stream:
        line = line.strip()
        if line == readymsg:
            break
        else:
            result.append(line)
    return result

completer_cache = {}
def completer_cache_val(v, f):
    if v not in completer_cache:
        completer_cache[v] = f()
    return completer_cache[v]

def completer(text, state):
    def get_locals():
        return exec_sync("echo('\\r\\n'.join(locals().keys()))")
    def get_dir(code):
        return exec_sync("echo('\\r\\n'.join(dir(%s)))" % code)
    if text == '':
        return None
    try:
        locs = completer_cache_val('locals', get_locals)
        if '.' in text:
            tokens = text.split('.')
            if len(tokens) > 2:
                return None
            if tokens[0] in locs:
                attrs = completer_cache_val('dir_' + tokens[0], lambda: get_dir(tokens[0]))
                return tokens[0]+'.'+[w for w in attrs if w.startswith(tokens[1])][state]
        else:
            return [w for w in locs if w.startswith(text)][state]
    except IndexError:
        return None

readline.set_completer(completer)
readline.parse_and_bind('tab: complete')

write_stream('__READYMSG = "%s"' % readymsg)
for line in stream:
    line = line.strip()
    if line == readymsg:
        cmd = raw_input('> ')
        write_stream(cmd.strip())
        completer_cache = {}
    else:
        print line

print 'connection closed'
