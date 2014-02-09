write_client = None

def run_repl():
    import socket
    global write_client

    port = 2222
    newline = '\r\n'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', port))
    s.listen(1)


    def repl(__f, once=False):
        global write_client

        def echo(s):
            __f.write(str(s))
            __f.write(newline)
            __f.flush()
        write_client = echo
        def doc(o):
            for line in o.__doc__.splitlines():
                echo(line)

        for _line in __f:
            _line = _line.strip()
            if _line == 'QUIT':
                break
            try:
                if len(_line) > 2:
                    if _line[0:2] == 'p ':
                        __f.write(repr(eval(_line[2:].strip())) + '\r\n')
                        __f.flush()
                    else:
                        exec _line in globals(), locals()
            except Exception, e:
                echo(e)
            if once:
                break

    try:
        conn, addr = s.accept()
        f = conn.makefile()
        repl(f)
    except Exception, e:
        print e
        import traceback
        traceback.print_stack()
    write_client = None
    conn.close()
    s.close()

if __name__ == '__main__':
    print 'run repl..'
    run_repl()
