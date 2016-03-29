import py_compile

try:
    import os
    import sys

    mods_path = './res_mods/mods'
    mods = os.listdir(mods_path + '/packages')
    print 'Trying to load following mods:'
    print mods
    sys.path.insert(0, mods_path + '/packages')

    for mod in mods:
        try:
	    path = '%s/packages/%s/' % (mods_path,mod)
	    if not os.path.exists(path+'__init__.pyc'):
	        with open(path+'__init__.py', 'w') as f:
	            pass
		py_compile.compile(path+'__init__.py')
                os.remove(path+'__init__.py')
            __import__(mod + '.python', globals(), locals(), [])
            print 'loaded ' + mod
        except:
            pass
except Exception, e:
    print 'Loader failed:',e
