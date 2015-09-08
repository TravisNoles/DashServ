#Handles digitalocean account information (GET)
#URL: https://api.digitalocean.com/v2/account


# Response Body (example)
# {
#   "account": {
#     "droplet_limit": 25,
#     "email": "sammy@digitalocean.com",
#     "uuid": "b6fr89dbf6d9156cace5f3c78dc9851d957381ef",
#     "email_verified": true
#   }
# }

import requests
import json
import os
from common import getHeader
from common import getStatusCode

#Returns all or specific digitalocean account information
def getAccount():
    #Set url to /account
    url = "https://api.digitalocean.com/v2/account"
    
    #Get headers from api.py and set local variable.
    headers = getHeader()
    
    #send a get request to the url, with custom auth headers.
    r = requests.get(url, headers=headers)

    #Returns results of account in JSON format.
    return r.text;


#Check remaining rate limit left on digital ocean account (resets every hour)
def checkRateLimit()

    ratelimit = getheader("ratelimit-remaining")
    
    print ratelimit
    return ratelimit


#Debug Functions