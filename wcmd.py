# command line tools for waveIDE

import os
import sys
import tempfile
from wirewave import *

def runwave(wid):
    """runs a wave specified by it's ID"""
    pass

def viewwave(wid):
    print "rendering "+wid
    w = WaveReader()
    w.read(wid)
    w.render()
    (h,fn) = tempfile.mkstemp(".html","wave")
    os.write(h,w.renderedHTML)
    os.close(h)
    os.startfile(fn)
    pass

def printhelp():
    print """Usage: wcmd.py [command] [arguments]
Usable wcmd commands:
   runwave [waveid]\t-runs the python code from specified wave   
   view [waveid]\t-Displays a wave in default browser
"""
    
if (len(sys.argv) < 2):
    printhelp()
    exit()
    pass
if (sys.argv[1] == "--help"):
    printhelp()
elif (sys.argv[1] == "runwave"):
    runwave(sys.argv[2])
elif (sys.argv[1] == "view"):
    viewwave(sys.argv[2])
else:
    print "wcmd: '"+sys.argv[1]+"' is not a valid command. See 'wcmd.py --help'"
