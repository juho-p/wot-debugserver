XPM_MOD_VERSION = '1.0.1'
XPM_MOD_URL = ''
XPM_MOD_UPDATE_URL = ''
XPM_GAME_VERSIONS = ['0.8.11']

run = True

import datetime
import tcprepl

def log(text):
    ds = datetime.time.strftime(datetime.datetime.now().time(), '%H:%M')
    try:
        with open('d:\log\log.txt', 'a') as f:
            f.write('%s: %s\n' % (ds, text))
    except:
        print 'error..'

def run_server():
    log('run server...')
    print 'run server...'
    tcprepl.run_repl()
    log('** server stopped!')

def set_stopper():
    from gui.Scaleform.Flash import Flash
    from gui.mods.xpm import RegisterEvent
    def close(*args, **kws):
        print 'close socket'
        tcprepl.closesocket()
    print 'setup stopper..'
    RegisterEvent(Flash, 'beforeDelete', close)

if run:
    log('starting..')

    try:
        import threading
        thread = threading.Thread(target=run_server, args=())
        thread.start()

        import BigWorld
        BigWorld.callback(1, set_stopper())

        log('thread started..')
    except:
        log('didnt work')
