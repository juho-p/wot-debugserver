XFW_MOD_VERSION = '1.3.0'
XFW_MOD_URL = ''
XFW_MOD_UPDATE_URL = ''
XFW_GAME_VERSIONS = ['0.9.6']

run = True

import datetime
import tcprepl

def log(text):
    ds = datetime.time.strftime(datetime.datetime.now().time(), '%H:%M')
    print 'replserver %s: %s' % (ds, text)

def run_server():
    log('run server...')
    try:
        while True:
            tcprepl.run_repl()
            log('REPL stopped, restarting...')
    except:
        log('* Crashed *')
        import traceback
        traceback.print_exc()
    log('Server stopped!')

if run:
    log('starting..')

    try:
        import threading
        thread = threading.Thread(target=run_server, args=())
        thread.setDaemon(True)
        thread.start()

        log('thread started..')
    except:
        import traceback
        traceback.print_exc()
