import os
import sys

def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))
