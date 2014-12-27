write_client = None

import socket

PORT = 2222

def run_repl():
    '''
    Run debug server until connection is closed
    '''
    global write_client

    newline = '\r\n'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', PORT))
    s.listen(1)

    def repl(filestream, once=False):
        global write_client
        import wotdbg

        def echo(s):
            filestream.write(str(s))
            filestream.write(newline)
            filestream.flush()
        write_client = echo

        local_vars = {'echo': echo, 'wotdbg': wotdbg}

        for line in filestream:
            line = line.strip()
            if line == 'QUIT':
                break
            try:
                try:
                    try_exec = False
                    res = eval(line, local_vars)
                    echo(res)
                except SyntaxError:
                    try_exec = True
                if try_exec:
                    exec line in local_vars
            except Exception, e:
                import traceback
                echo(traceback.format_exc())
            readymsg = local_vars.get('__READYMSG', None)
            if readymsg is not None:
                echo(readymsg)
            if once:
                break
        write_client = None

    conn = f = None
    try:
        conn, addr = s.accept()
        f = conn.makefile()
        repl(f)
    finally:
        s.close()
        if conn != None:
            conn.close()
            f.close()

if __name__ == '__main__':
    run_repl()
