here=`dirname $0`

cd "$here"

python -m compileall .

resmods='../../../..'

# pretty crap, but whatever
lastversion=`(cd $resmods && ls | grep '^[0-9]\.[0-9]' | sort -V | tail -n1)`

installdir="$resmods/$lastversion/scripts/client/gui/mods/"
mkdir -pv "$installdir"
cp -v mod_.pyc "$installdir"
