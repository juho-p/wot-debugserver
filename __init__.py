XPM_MOD_VERSION = '1.0.1'
XPM_MOD_URL = ''
XPM_MOD_UPDATE_URL = ''
XPM_GAME_VERSIONS = ['0.8.10']

run = False

import datetime

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
    import tcprepl
    tcprepl.run_repl()
    log('** server stopped!')

if run:
    log('starting..')

    try:
        import threading
        thread = threading.Thread(target=run_server, args=())
        thread.start()
        log('thread started..')
    except:
        log('didnt work')
