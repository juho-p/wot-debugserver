here=`dirname $0`

cd "$here"

python -m compileall .

resmods='../../../..'

# pretty crap, but whatever
lastversion=`(cd $resmods && ls | grep '^[0-9]\.[0-9]' | sort -V | tail -n1)`

cp -v mod_.pyc $resmods/$lastversion/scripts/client/gui/mods/
