#!/usr/bin/python

import socket
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
    def get_path_dir(locs, path):
        attrs = locs
        for i, token in enumerate(path):
            if token in attrs:
                attrs = get_dir('.'.join(start[0:i+1]))
            else:
                return []
        return attrs

    if text == '':
        return None
    try:
        locs = completer_cache_val('locals', get_locals)
        if '.' in text:
            tokens = text.split('.')
            start = tokens[0:-1]
            last = tokens[-1]

            attrs = completer_cache_val('dir_' + '.'.join(start), lambda: get_path_dir(locs, start))

            suggestion = [w for w in attrs if w.startswith(last)][state]
            return '.'.join(start + [suggestion])
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
