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

First, compile .py files to .pyc files using either build.cmd (for Windows
users) or build.sh (Linux and Cygwin users)

Then, if you have XVM installed:

Copy `__init__.pyc` and `tcprepl.pyc` under
`res_mods/0.8.11/scripts/client/gui/mods/replserver`
(create the replserver-folder under mods-folder)

If you don't have XVM installed, then you should download xvm mod and at least copy following files from it to your `res_mods`-folder:

  * `scripts/client/gui/scaleform/locale/__init__.pyc`
  * `scripts/client/gui/mods/__init__.pyc`
  * `scripts/client/gui/mods/xpm.pyc`

These files ensure that the mod loads correctly

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

    > p 'hello'
    'hello'
    > import messenger
    > gui = messenger.MessengerEntry.g_instance.gui
    > gui.addClientMessage('hello gui', True) # try this when in battle
    > import BigWorld
    > p BigWorld.player().name # displays player nickname
    'awesome-mod-creator'
    > QUIT

Notes:

* To execute python code, just type it in the console
* If you type an expression, the evaluated result will get printed
* To echo something to client, use echo function that is visible to REPL
* If you use print to write something to STDOUT, it is written to python.log-file
* To stop the server, type `QUIT`
* If you have problems, see what's in python.log file that's created in WOT directory

