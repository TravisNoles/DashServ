#This file handles locations to files and directories.
#File is not currently used please see settings.yaml in your config directory.

import os
import sys
import json
import getpass

#Configure Paths
__BASE_DIR = os.path.dirname(os.getcwd()) + "/ServDash"
__USERNAME = getpass.getuser()

#Return Paths
def getBasePath():
    return __BASE_DIR
    
def getUsernameSys():
    return __USERNAME
    
def getConfigLocationDigitalOcean():
    return __CONFIG_DIGTIALOCEAN
    
def getRunPath():
    return __RUN_PATH


apikey = getAuthKey()
print apikey