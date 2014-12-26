XPM_MOD_VERSION = '1.2.0'
XPM_MOD_URL = 'https://github.com/juho-p/wot-debugserver'
XPM_MOD_UPDATE_URL = ''
XPM_GAME_VERSIONS = ['0.9.5']

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
