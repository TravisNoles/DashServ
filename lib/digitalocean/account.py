import requests
import json
import os
from config import geturl
from config import getapikey
from config import getbasepath
from config import getheader

# User information methods

#User - User Status (active, warning or locked)
#User Status - Detailed human readable message
#User - Get droplet_limit
#User - Email verified.


BASE_PATH = getbasepath()
BASE_URL = geturl("digitalocean")
API_KEY = getapikey("digitalocean")

# Get and return headers as JSON 
def getauth(params=""):
    #Headers to send with API Key
    headers = getheader()
    r = requests.get(BASE_URL, headers=headers)
    return headers[params]

#Check remaining rate limit left on digital ocean account (resets every hour)
def checkratelimit(provider):
    ratelimit = getheader("ratelimit-remaining")
    
    print ratelimit
    return ratelimit

