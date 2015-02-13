wot-debugserver
===============

This is a mod for World of Tanks to make development easier. When installed, it
spawns server thread in background that listens for local TCP connection to
provide REPL interface to BigWorld engine. This might be useful for trying how
things work in BigWorld engine before you implement the functionality in a mod.

Getting started
===============

Step 1: Setup server
--------------------

It is easiest to have XVM installed. If you don't then see the note below.

You need to have required `.pyc` files in
`res_mods/mods/packages/wot-debugserver/python/` -folder. Compile all `.py`
files using build.cmd script and copy resulting files to that folder.

If you have Cygwin and git and python2.7 installed (or are using Linux or some
other environment where you have bash and git), you can use following commands:

    cd /path/to/World_of_Tanks/
    cd res_mods/mods/packages
    # I clone to replserver because it sounds nicer than wot-debugserver
    git clone git clone https://github.com/juho-p/wot-debugserver.git replserver
    cd replserver
    python -m compileall .

NOTE: Everything is easier if you have XVM installed. If not, then you have to
find another way to run the REPL. Basically you have to compile python files to
pyc-files and somehow import the resulting module during WOT-startup

Step 2: Start game
------------------

Start the game. Hopefully the server starts

Step 3: Connect to the console
------------------------------

Two ways to connect: Using raw TCP-client or using client.py

You can connect to the server using basic TCP connection. You can use for
example netcat or PuTTY (with raw-mode) to start the connection. Use
`localhost` as host and port `2222` for the connection. I think standard telnet
client also works for this

If you want **autocomplete** -feature (who doesn't?), then you should instead
use client.py that comes with this mod. But before you start, you should get
readline module working with Python. In Windows, easiest way to do this is
install Cygwin (install at least python package). If you use a good OS, like
Linux, then you don't need to install anything (if using any sensible
distribution...)

To use client.py, just run `python client.py` and it should automatically
connect. If not, then the server mod did not start for some reason.

Example usage
-------------

Best way to try this is to start some replay and try different things when the
game is running

    > 'hello'
    'hello'
    > import messenger
    > gui = messenger.MessengerEntry.g_instance.gui
    > gui.addClientMessage('hello gui', True) # try this when in battle
    > import BigWorld
    > BigWorld.player().name # displays player nickname
    'awesome-mod-creator'
    > QUIT

Notes:

* To execute python code, just type it in the console
* If you type an expression, the evaluated result will get printed
* To echo something to client, use echo function that is visible to REPL
* If you use print to write something to STDOUT, it is written to python.log-file
* To stop the server, type `QUIT`
* If you have problems, see what's in python.log file that's created in WOT directory

