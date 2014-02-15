XPM_MOD_VERSION = '1.0.2'
XPM_MOD_URL = ''
XPM_MOD_UPDATE_URL = ''
XPM_GAME_VERSIONS = ['0.8.11']

run = True

import datetime
import tcprepl

def log(text):
    ds = datetime.time.strftime(datetime.datetime.now().time(), '%H:%M')
    print 'replserver %s: %s' % (ds, text)

def run_server():
    log('run server...')
    tcprepl.run_repl()
    log('** server stopped!')

def set_stopper():
    from gui.Scaleform.Flash import Flash
    from gui.mods.xpm import RegisterEvent
    def close(*args, **kws):
        log('close socket')
        tcprepl.closesocket()
    RegisterEvent(Flash, 'beforeDelete', close)

if run:
    log('starting..')

    try:
        import threading
        thread = threading.Thread(target=run_server, args=())
        thread.start()

        import BigWorld
        BigWorld.callback(1, set_stopper)

        log('thread started..')
    except:
        import traceback
        traceback.print_exc()
